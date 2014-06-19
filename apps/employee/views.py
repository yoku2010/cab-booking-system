from django.views.generic import TemplateView, View, RedirectView
from django.template.loader import render_to_string
from django.middleware.csrf import get_token

from libs.jsonresponse import JSONResponseMixin

# Create your views here.
class CabBookingView(View, JSONResponseMixin):
    '''
    @summary: Add User
    '''
    template_name = 'employee/cab_booking.html'

    def get(self, request, *args, **kwargs):
        data = {}
        #add_form = self.add_user()
        context = {}#{'action': 'add','form' : add_form['form'], 'csrf_token_value': get_token(self.request)}
        data['status'] = 1
        data['html'] = render_to_string(self.template_name, context)
        return self.render_to_response(data)

    def post(self, request, *args, **kwargs):
        data = {}#self.add_user(self.request.POST)
        return self.render_to_response(data)
