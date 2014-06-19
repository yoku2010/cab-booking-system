# import django packages
from django.views.generic import TemplateView, View, RedirectView
from django.template.loader import render_to_string
from django.middleware.csrf import get_token

# import libraries
from libs.jsonresponse import JSONResponseMixin
from apps.frontend.utils import CommonLoginForm, CommonLogout, ManageUser, Feedback

# Create your views here.
# Template View
class HomeView(TemplateView, CommonLoginForm):
    '''
    @summary: Home page
    '''
    template_name = 'frontend/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['login_form'] = self.get_login_form()
        context['head_text'] = 'CAB Booking'
        context['subhead_text'] = 'Corporate Account'
        context['para_text'] = 'Our value added services for you..'
        context['menu'] = 'home'
        if self.request.user.is_authenticated():
            groups = [g.name for g in self.request.user.groups.all()]
            if 'employee' in groups:
                context['group'] = 'employee'
            elif 'employee_manager' in groups:
                context['group'] = 'employee_manager'
            elif 'manager' in groups:
                context['group'] = 'manager'
            elif 'admin' in groups:
                context['group'] = 'admin'
        return context


class AboutUsView(TemplateView):
    '''
    @summary: About Us page
    '''
    template_name = 'frontend/about_us.html'

    def get_context_data(self, **kwargs):
        context = super(AboutUsView, self).get_context_data(**kwargs)
        context['head_text'] = 'About Us'
        context['subhead_text'] = 'We think you\'ll love to work with us'
        context['para_text'] = 'Our value added services for you..'
        context['menu'] = 'about-us'
        return context


class ServicesView(TemplateView):
    '''
    @summary: Services page
    '''
    template_name = 'frontend/services.html'

    def get_context_data(self, **kwargs):
        context = super(ServicesView, self).get_context_data(**kwargs)
        context['head_text'] = 'Our Services'
        context['subhead_text'] = 'We can handle anything you need. Check out our services below!'
        context['para_text'] = 'Our value added services for you..'
        context['menu'] = 'services'
        return context


class ContactsView(TemplateView):
    '''
    @summary: Contacts page
    '''
    template_name = 'frontend/contacts.html'

    def get_context_data(self, **kwargs):
        context = super(ContactsView, self).get_context_data(**kwargs)
        context['head_text'] = 'Get In Touch'
        context['subhead_text'] = 'We\'re just an email or phone call away!'
        context['para_text'] = 'Our value added services for you..'
        context['menu'] = 'contacts'
        return context


class PrivacyPolicyView(TemplateView):
    '''
    @summary: Privacy Policy page
    '''
    template_name = 'frontend/privacy_policy.html'

    def get_context_data(self, **kwargs):
        context = super(PrivacyPolicyView, self).get_context_data(**kwargs)
        context['head_text'] = 'Privacy Policy'
        context['subhead_text'] = 'We think you\'ll love to work with us'
        context['para_text'] = 'Our value added services for you..'
        context['menu'] = 'privacy_policy'
        return context


class TermsAndConditionsView(TemplateView):
    '''
    @summary: Terms and Conditions page
    '''
    template_name = 'frontend/terms_and_conditions.html'

    def get_context_data(self, **kwargs):
        context = super(TermsAndConditionsView, self).get_context_data(**kwargs)
        context['head_text'] = 'Terms and Conditions'
        context['subhead_text'] = 'We think you\'ll love to work with us'
        context['para_text'] = 'Our value added services for you..'
        context['menu'] = 'terms_and_conditions'
        return context


class UserLogin(View, JSONResponseMixin, CommonLoginForm):
    '''
    @summary: Common login form submit (for employee, employee manager, manager, admin).
    '''
    def post(self, request, *args, **kwargs):
        data = self.post_login_form(request)
        return self.render_to_response(data)


class UserLogout(RedirectView, CommonLogout):
    '''
    @summary: logout user and will return on home page
    '''
    def get(self, request, *args, **kwargs):
        self.url = self.user_logout(request)    # will return the home page url
        return super(UserLogout, self).get(self, request, *args, **kwargs)


class GetUsersView(View, JSONResponseMixin, ManageUser):
    '''
    @summary: To get user data in table.
    '''
    def get(self, request, *args, **kwargs):
        data = self.get_users()
        return self.render_to_response(data)

class AddUserFormView(View, JSONResponseMixin, ManageUser):
    '''
    @summary: Add User
    '''
    template_name = 'frontend/user_form.html'
    def get(self, request, *args, **kwargs):
        data = {}
        add_form = self.add_user()
        context = {'action': 'add','form' : add_form['form'], 'csrf_token_value': get_token(self.request)}
        data['html'] = render_to_string(self.template_name, context)
        return self.render_to_response(data)

    def post(self, request, *args, **kwargs):
        data = self.add_user(self.request.POST)
        return self.render_to_response(data)


class EditUserFormView(View, JSONResponseMixin, ManageUser):
    '''
    @summary: Edit User
    '''
    template_name = 'frontend/user_form.html'
    def get(self, request, *args, **kwargs):
        data = {}
        user_id = self.request.GET.get('user_id')
        edit_form = self.edit_user(user_id)
        context = {'action': 'edit', 'form' : edit_form['form'], 'csrf_token_value': get_token(self.request)}
        data['status'] = 1
        data['html'] = render_to_string(self.template_name, context)
        return self.render_to_response(data)

    def post(self, request, *args, **kwargs):
        data = self.update_user(self.request.POST)
        return self.render_to_response(data)


class DeleteUserView(View, JSONResponseMixin, ManageUser):
    '''
    @summary: Delete User
    '''
    def get(self, request, *args, **kwargs):
        user_id = self.request.GET.get('user_id')
        data = self.delete_user(user_id)
        return self.render_to_response(data)

class FeedbackFormView(View, JSONResponseMixin, Feedback):
    '''
    @summary: Feedback Form
    '''
    template_name = 'frontend/feedback_form.html'
    def get(self, request, *args, **kwargs):
        data = {}
        form_dt = self.feedback_form()
        context = {'form' : form_dt, 'csrf_token_value': get_token(self.request)}
        data['html'] = render_to_string(self.template_name, context)
        return self.render_to_response(data)

    def post(self, request, *args, **kwargs):
        data = {}
        dt = self.save_form(self.request)
        if dt:
            data['status'] = 1
            data['message'] = 'Feedback Submitted Successfully.'
        else:
            data['status'] = 0
            data['message'] = 'Data is missing'
        return self.render_to_response(data)

class FeedbackListView(View, JSONResponseMixin, Feedback):
    '''
    @summary: Feedback List
    '''
    template_name = 'frontend/feedback_list.html'
    def get(self, request, *args, **kwargs):
        context = { 'feedback': self.get_feedback_list() }
        data = {'status': 1, 'html': render_to_string(self.template_name, context) }
        return self.render_to_response(data)
