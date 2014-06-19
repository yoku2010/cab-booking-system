from django.views.generic import TemplateView, View, RedirectView
from django.template.loader import render_to_string
from django.middleware.csrf import get_token

from libs.jsonresponse import JSONResponseMixin
from models import CabBooking, EmployeeManager

# Create your views here.
class CabBookingView(View, JSONResponseMixin):
    '''
    @summary: Cab Booking
    '''
    template_name = 'employee/cab_booking.html'

    def get(self, request, *args, **kwargs):
        data = {}
        context = {'csrf_token_value': get_token(self.request)}
        data['status'] = 1
        data['html'] = render_to_string(self.template_name, context)
        return self.render_to_response(data)

    def post(self, request, *args, **kwargs):
        data = {}#self.add_user(self.request.POST)
        post_dt = self.request.POST
        booking_type = post_dt.get('type')
        if 'Local' == booking_type:
            cb = CabBooking(user = self.request.user, booking_type = booking_type, duration = post_dt.get('duration'), reason = post_dt.get('reason'), date = post_dt.get('pickup_date'), time = post_dt.get('pickup_time'), start = post_dt.get('from_city'))
            cb.save()
            data['status'] = 1
            data['message'] = 'Cab booked successfully.'
        elif 'Airport' == booking_type:
            cb = CabBooking(user = self.request.user, booking_type = booking_type, reason = post_dt.get('reason'), date = post_dt.get('pickup_date'), time = post_dt.get('pickup_time'), start = post_dt.get('want_car_for'), end = post_dt.get('city'))
            cb.save()
            data['status'] = 1
            data['message'] = 'Cab booked successfully.'
        elif 'Outstation' == booking_type:
            cb = CabBooking(user = self.request.user, booking_type = booking_type, reason = post_dt.get('reason'), date = post_dt.get('pickup_date'), time = post_dt.get('pickup_time'), start = post_dt.get('from_city'), end = post_dt.get('to_city'))
            cb.save()
            data['status'] = 1
            data['message'] = 'Cab booked successfully.'
        else:
            data['status'] = 0
            data['message'] = 'Invalid Type of booking'
        return self.render_to_response(data)

class BookedCabListView(View, JSONResponseMixin):
    '''
    @summary: List of booked cab
    '''
    template_name = 'employee/cab_booking_list.html'

    def get(self, request, *args, **kwargs):
        data = {}
        data['status'] = 1
        context = {"local": CabBooking.objects.filter(booking_type = 'Local', user = self.request.user)}
        context["airport"] = CabBooking.objects.filter(booking_type = 'Airport', user = self.request.user)
        context["out_station"] = CabBooking.objects.filter(booking_type = 'Outstation', user = self.request.user)
        data['html'] = render_to_string(self.template_name, context)
        return self.render_to_response(data)
        

class DeleteBookedCab(View, JSONResponseMixin):
    '''
    @summary: Delete Booked Cab
    '''
    def get(self, request, *args, **kwargs):
        data = {}
        booking_id = self.request.GET.get('booking_id')
        bc = CabBooking.objects.filter(id = booking_id)
        if bc:
            bc.delete()
            data['status'] = 1
            data['message'] = 'Booked cab canceled successfully.'
        else:
            data['status'] = 0
            data['message'] = 'Record not found.'
        return self.render_to_response(data)


class ApproveCabListView(View, JSONResponseMixin):
    '''
    @summary: List of booked cab
    '''
    template_name = 'employee/cab_booking_list_approve.html'

    def get(self, request, *args, **kwargs):
        data = {}
        data['status'] = 1
        user_list = [e.employee for e in EmployeeManager.objects.filter(manager = self.request.user)]
        context = {"local": CabBooking.objects.filter(booking_type = 'Local', user__in = user_list, status = 0)}
        context["airport"] = CabBooking.objects.filter(booking_type = 'Airport', user__in = user_list, status = 0)
        context["out_station"] = CabBooking.objects.filter(booking_type = 'Outstation', user__in = user_list, status = 0)
        data['html'] = render_to_string(self.template_name, context)
        return self.render_to_response(data)

class ApproveBookedCab(View, JSONResponseMixin):
    '''
    @summary: Approve Booked Cab
    '''
    def get(self, request, *args, **kwargs):
        data = {}
        booking_id = self.request.GET.get('booking_id')
        bc = CabBooking.objects.filter(id = booking_id)
        if bc:
            bc = bc[0]
            bc.status = 1;
            bc.save()
            data['status'] = 1
            data['message'] = 'Booked cab approved successfully.'
        else:
            data['status'] = 0
            data['message'] = 'Record not found.'
        return self.render_to_response(data)

class ApproveCabListTwoView(View, JSONResponseMixin):
    '''
    @summary: List of booked cab
    '''
    template_name = 'employee/cab_booking_list_approve.html'

    def get(self, request, *args, **kwargs):
        data = {}
        data['status'] = 1
        context = {"local": CabBooking.objects.filter(booking_type = 'Local', status = 1)}
        context["airport"] = CabBooking.objects.filter(booking_type = 'Airport', status = 1)
        context["out_station"] = CabBooking.objects.filter(booking_type = 'Outstation', status = 1)
        data['html'] = render_to_string(self.template_name, context)
        return self.render_to_response(data)

class ApproveBookedCabTwo(View, JSONResponseMixin):
    '''
    @summary: Approve Booked Cab 2
    '''
    def get(self, request, *args, **kwargs):
        data = {}
        booking_id = self.request.GET.get('booking_id')
        bc = CabBooking.objects.filter(id = booking_id)
        if bc:
            bc = bc[0]
            bc.status = 2;
            bc.save()
            data['status'] = 1
            data['message'] = 'Booked cab approved successfully.'
        else:
            data['status'] = 0
            data['message'] = 'Record not found.'
        return self.render_to_response(data)
