# import django packages
from django.contrib.auth import logout
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

# import apps
from apps.frontend.forms import LoginForm, UserForm
from apps.employee.models import EmployeeManager

# utility classes
class UserProfilePage(object):
    '''
    @summary: To get user profile page url by their group
    '''
    def get_profile_page_url(self, user):
        groups = [g.name for g in user.groups.all()]
        page_url = reverse('home')

        if 'employee' in groups:
            page_url = reverse('home')
        elif 'employee_manager' in groups:
            page_url = reverse('home')
        elif 'manager' in groups:
            page_url = reverse('home')
        elif 'admin' in groups:
            page_url = reverse('home')
        return page_url

class CommonLoginForm(UserProfilePage):
    '''
    @summary: Common login
    '''
    form_class = LoginForm

    def get_login_form(self):
        return self.form_class()

    def post_login_form(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        response_data = {}
        if form.is_valid():
            user = form.authenticate(request)
            if user:
                response_data['status'] = 1
                response_data['message'] = "User logged in successfully."
                response_data['url'] = self.get_profile_page_url(user)
            else:
                response_data['status'] = 3
                response_data['message'] = "Invalid employee id or password."
        else:
            response_data['status'] = 0
            response_data['message'] = "Employee id and password required."
            response_data['data'] = form.errors
        return response_data

class CommonLogout(object):
    '''
    @summary: Common logout
    '''
    def user_logout(self, request):
        logout(request)             # logout user
        return reverse('home')      # get the home page url
        
class ManageUser(object):
    '''
    @summary: Get User Details
    '''
    def get_users (self):
        status = 0
        message = 'No users exists.'
        dt_list = []
        users = User.objects.all()
        i = 0
        if users:
            for u in users:
                i += 1
                groups = [' '.join(g.name.split('_')).title() for g in u.groups.all()]
                dt_list.append([
                    i,
                    u.first_name,
                    u.last_name,
                    u.username,
                    u.email,
                    groups,
                    [('%s %s' % (e.manager.first_name and e.manager.first_name or e.manager.username, e.manager.last_name and e.manager.last_name or '')).title() for e in EmployeeManager.objects.filter(employee = u.id)],
                    (True, False)['Admin' in groups],
                    u.id
                ])
            status = 1
            message = ""
        data = {
            'status': status,
            'message': message,
            'data': dt_list
        }
        return data
        
    def add_user (self, data = {}):
        if data:
            form = UserForm(data)
            if form.is_valid():
                form.save()
                return {'status': 1, 'message': 'User Added successfully'}
            else:
                return {'status': 0, 'error': form.errors, 'message': 'Form submitted with invalid data. Please try again.' }
        else:
            form = UserForm()
            return {'status': 1, 'form': form}

    def update_user (self, data):
        if data:
            form = UserForm(data)
            if form.is_valid():
                return form.update()
        return {'status': 0, 'error': form.errors, 'message': 'Form submitted with invalid data. Please try again.' }

    def edit_user (self, user_id):
        data = {}
        user = User.objects.filter(id = user_id)
        if user:
            user = user[0]
            group = ''.join([g.name for g in user.groups.all()])
            manager = EmployeeManager.objects.filter(employee = user)
            if manager:
                manager = manager[0]
                manager = manager.manager.id
            else:
                manager = 0
            form = UserForm({
                'user_id': user.id,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'email': user.email,
                'employee_id': user.username,
                'password': '',
                'group': group,
                'manager': manager,
                })
            data['status'] = 1
            data['form'] = form
        else:
            data['status'] = 0
            data['message'] = 'User does not exist. Please try again'
        return data

    def delete_user (self, user_id):
        data = {}
        user = User.objects.filter(id = user_id)
        if user:
            user.delete()
            data['status'] = 1
            data['message'] = 'User has been deleted successfully'
        else:
            data['status'] = 0
            data['message'] = 'User does not exist. Please try again'
        return data
