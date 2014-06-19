import json
from django.http import HttpResponse

class JSONResponseMixin(object):
    '''
    A mixin that can be used to render a JSON response.
    '''
    def render_to_response(self, context, **response_kwargs):
        '''
        Returns a JSON response containing 'context' as payload
        '''
        return self.render_to_json_response(context, **response_kwargs)

    def render_to_json_response(self, context, **response_kwargs):
        '''
        Returns a JSON response, transforming 'context' to make the payload.
        '''
        return HttpResponse(
            self.convert_context_to_json(context),
            content_type='application/json',
            **response_kwargs
        )

    def convert_context_to_json(self, context):
        '''
        Convert the context dictionary into a JSON object
        '''
        # Note: This is *EXTREMELY* naive; in reality, you'll need
        # to do much more complex handling to ensure that arbitrary
        # objects -- such as Django model instances or querysets
        # -- can be serialized as JSON.
        return json.dumps(context)