from django.conf.urls import patterns, url

from views import HomeView, AboutUsView, ServicesView, ContactsView, PrivacyPolicyView, TermsAndConditionsView, \
UserLogin, UserLogout, GetUsersView, AddUserFormView, DeleteUserView, EditUserFormView, FeedbackFormView, FeedbackListView

urlpatterns = patterns("apps.frontend",
    url(r'^$', HomeView.as_view(), name = 'home'),
    url(r'^about-us/$', AboutUsView.as_view(), name = 'about-us'),
    url(r'^services/$', ServicesView.as_view(), name = 'services'),
    url(r'^contacts/$', ContactsView.as_view(), name = 'contacts'),
    url(r'^privacy-policy/$', PrivacyPolicyView.as_view(), name = 'privacy-policy'),
    url(r'^terms-and-conditions/$', TermsAndConditionsView.as_view(), name = 'terms-and-conditions'),
    url(r'^user-login/$', UserLogin.as_view(), name = 'user-login'),
    url(r'^user-logout/$', UserLogout.as_view(), name = 'user-logout'),
    url(r'^get-users/$', GetUsersView.as_view(), name = 'get-users'),
    url(r'^add-user/$', AddUserFormView.as_view(), name = 'add-user'),
    url(r'^delete-user/$', DeleteUserView.as_view(), name = 'delete-user'),
    url(r'^edit-user/$', EditUserFormView.as_view(), name = 'edit-user'),
    url(r'^feedback/$', FeedbackFormView.as_view(), name = 'feedback'),
    url(r'^feedback-list/$', FeedbackListView.as_view(), name = 'feedback-list'),
)