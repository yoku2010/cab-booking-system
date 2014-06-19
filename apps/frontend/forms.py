from django import forms
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout
from apps.frontend.lookups import get_group_choices, get_user_choices
from apps.employee.models import EmployeeManager


from models import FeedbackModel

feedback_subjects = (('', '- Select Subject -'),('Query', 'Query'), ('Suggestion', 'Suggestion'), ('Complaint', 'Complaint'), ('Feedback', 'Feedback'))
class LoginForm(forms.Form):
    email = forms.CharField(label='Employee ID', widget=forms.TextInput(attrs={'placeholder': 'Enter your employee id', 'icon': 'fa-envelope-o'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password', 'icon': 'fa-key'}))

    def authenticate(self, request = None):
        logout(request)                             # logout other user
        data = self.cleaned_data
        user = authenticate(username = data['email'], password = data['password'])
        if user is not None:
            login(request, user)                    # login user
        return user

class FeedbackForm(forms.Form):
    subject = forms.ChoiceField(label='Subject', widget=forms.Select(), choices = feedback_subjects)
    body = forms.CharField(label='Body', widget=forms.Textarea(attrs={'placeholder': 'Enter your text'}))

    def save(self, request = None):
        data = self.cleaned_data
        fd = FeedbackModel(user = request.user, subject = data['subject'], body = data['body'], email = request.user.email)
        fd.save()
        return True

class UserForm(forms.Form):
    user_id = forms.CharField(widget=forms.HiddenInput(), required = False)
    first_name = forms.CharField(label='First Name', widget=forms.TextInput(attrs={'placeholder': 'Enter first name'}))
    last_name = forms.CharField(label='Last Name', widget=forms.TextInput(attrs={'placeholder': 'Enter last name'}))
    email = forms.CharField(label='Email', widget=forms.EmailInput(attrs={'placeholder': 'Enter email'}))
    employee_id = forms.CharField(label='Employee Id', widget=forms.TextInput(attrs={'placeholder': 'Enter employee id'}))
    password = forms.CharField(label='Password', required = False, widget=forms.PasswordInput(attrs={'placeholder': 'Enter password'}))
    group = forms.ChoiceField(label = 'Group', widget = forms.Select(), choices = get_group_choices(), initial = '')
    manager = forms.ChoiceField(label = 'Manager', widget = forms.Select(), choices = get_user_choices(), initial = '')

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['manager'] = forms.ChoiceField(choices=get_user_choices())

    def save(self):
        data = self.cleaned_data
        user = User(first_name = data['first_name'], last_name = data['last_name'], email = data['email'], username = data['employee_id'])
        user.set_password(data['password'])
        user.save()
        g = Group.objects.get(name = data['group'])
        g.user_set.add(user)

        em = EmployeeManager(employee_id = user.id, manager_id = data['manager'])
        em.save()
        return True

    def update(self):
        data = self.cleaned_data
        user = User.objects.filter(id = data['user_id'])
        if user:
            user = user[0]
            user.first_name = data['first_name']
            user.last_name = data['last_name']
            user.email = data['email']
            user.username = data['employee_id']
            if data['password']:
                user.set_password(data['password'])
            user.save()

            group = ''.join([g.name for g in user.groups.all()])
            if group != data['group']:
                g = Group.objects.get(name = group)
                g.user_set.remove(user)

                g = Group.objects.get(name = data['group'])
                g.user_set.add(user)

            em = EmployeeManager.objects.filter(employee_id = data['user_id'])
            if em:
                em = em[0]
                em.manager_id = data['manager']
                em.save()
            else:
                em = EmployeeManager(employee_id = data['user_id'], manager_id = data['manager'])
                em.save()
            return {'status': 1, 'message': 'User Updated successfully'}
        else:
            return {'status': 0, 'message': 'User does not exist.'}

