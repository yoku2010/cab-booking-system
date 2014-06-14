# import django packages
from django.contrib.auth import logout
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

# import apps
from apps.frontend.forms import LoginForm

# utility classes
class UserProfilePage(object):
    '''
    @summary: To get user profile page url by their group
    '''
    def get_profile_page_url(self, user):
        groups = [g.name for g in user.groups.all()]
        page_url = reverse('home')

        if 'employee' in groups:
            page_url = ''#reverse('candidate-dashboard')
        elif 'manager' in groups:
            page_url = ''#reverse('college-dashboard')
        elif 'admin' in groups:
            page_url = ''#reverse('company-dashboard')
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
                response_data['message'] = SUCCESS['LOGIN']
                response_data['url'] = self.get_profile_page_url(user)
            else:
                response_data['status'] = 3
                response_data['message'] = ERROR['INVALID_LOGIN_FORM']
        else:
            response_data['status'] = 0
            response_data['message'] = ERROR['REQUIRE_LOGIN_CREDENTIALS']
            response_data['data'] = form.errors
        return response_data
        