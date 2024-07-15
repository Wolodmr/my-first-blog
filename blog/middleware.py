# blog/middleware.py

from django.utils.deprecation import MiddlewareMixin

class CustomMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # Custom logic for processing requests
        pass

    def process_response(self, request, response):
        # Custom logic for processing responses
        return response
