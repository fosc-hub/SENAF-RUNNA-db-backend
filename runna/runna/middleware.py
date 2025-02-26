
from threading import local

_thread_locals = local()

def get_current_authenticated_user():
    return getattr(_thread_locals, 'user', None)

class ThreadLocalMiddleware:
    """
    Middleware to store the current request user in thread-local storage.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        _thread_locals.user = getattr(request, 'user', None)
        return self.get_response(request)