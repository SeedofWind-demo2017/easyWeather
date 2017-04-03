
"""
Handle some Exceptions which we consider to be normal, e.g.
SiphonProfile.DoesNotExist so that we can avoid sending
an alert email about them.
"""

from django.shortcuts import render_to_response
from django.template import RequestContext

class ExceptionManager(object):
    def process_exception(self, request, exception):
        # Ignore SiphonProfile generated for logged-in staff
        # users, since staff don't need to have a SiphonProfile. All other
        # cases should be handled normally.
        if (request.user.is_authenticated() and request.user.is_staff and
            isinstance(exception, SiphonProfile.DoesNotExist)):
            return render_to_response('account/need_profile.html',
                                      {}, context_instance=RequestContext(request))
        # Otherwise, let processing continue as normal
        return None


class ExceptionLoggingMiddleware(object):
    def process_exception(self, request, exception):
        import traceback
        print traceback.format_exc()
