from django.contrib.auth import logout
from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

@method_decorator(csrf_exempt, name='dispatch')
class CustomLogoutView(View):
    def post(self, request, *args, **kwargs):
        """
        Logs out the currently authenticated user by clearing the session and cookies.
        """
        logout(request)  # Clear the session data
        response = JsonResponse({'message': 'Logout successful'}, status=200)

        # Remove the sessionid cookie
        response.delete_cookie(
            'sessionid', 
            path='/', 
            domain=None
        )
        return response
