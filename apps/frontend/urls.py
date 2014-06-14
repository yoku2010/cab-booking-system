from django.conf.urls import patterns, url

from views import HomeView, AboutUsView, ServicesView, ContactsView, PrivacyPolicyView, TermsAndConditionsView

urlpatterns = patterns("apps.frontend",
    url(r'^$', HomeView.as_view(), name = 'home'),
    url(r'^about-us/$', AboutUsView.as_view(), name = 'about-us'),
    url(r'^services/$', ServicesView.as_view(), name = 'services'),
    url(r'^contacts/$', ContactsView.as_view(), name = 'contacts'),
    url(r'^privacy-policy/$', PrivacyPolicyView.as_view(), name = 'privacy-policy'),
    url(r'^terms-and-conditions/$', TermsAndConditionsView.as_view(), name = 'terms-and-conditions'),
)