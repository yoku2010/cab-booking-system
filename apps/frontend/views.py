# import django packages
from django.views.generic import TemplateView, View, RedirectView

# import libraries
from apps.frontend.utils import CommonLoginForm

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

