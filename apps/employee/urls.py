from django.conf.urls import patterns, url

from views import CabBookingView, BookedCabListView, DeleteBookedCab, ApproveCabListView, ApproveBookedCab, \
ApproveCabListTwoView, ApproveBookedCabTwo

urlpatterns = patterns("apps.employee",
    url(r'^cab-booking/$', CabBookingView.as_view(), name = 'cab-booking'),
    url(r'^booked-cab-list/$', BookedCabListView.as_view(), name = 'booked-cab-list'),
    url(r'^delete-booking-cab/$', DeleteBookedCab.as_view(), name = 'delete-booking-cab'),
    url(r'^approve-cab-list/$', ApproveCabListView.as_view(), name = 'approve-cab-list'),
    url(r'^approve-booking-cab/$', ApproveBookedCab.as_view(), name = 'approve-booking-cab'),
    url(r'^approve-cab-list-2/$', ApproveCabListTwoView.as_view(), name = 'approve-cab-list-2'),
    url(r'^approve-booking-cab-2/$', ApproveBookedCabTwo.as_view(), name = 'approve-booking-cab-2'),
)