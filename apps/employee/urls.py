from django.conf.urls import patterns, url

from views import CabBookingView

urlpatterns = patterns("apps.employee",
    url(r'^cab-booking/$', CabBookingView.as_view(), name = 'cab-booking'),
)