import logging
from django.http import JsonResponse

logger = logging.getLogger(__name__)

class Handle500ErrorMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            response = self.get_response(request)
        except Exception as ex:
            logger.error(f'Error 500: {str(ex)}')
            return JsonResponse({'error': 'Internal Server Error', 'details': str(ex)}, status=500)
        return response
