
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
import json

@method_decorator(csrf_exempt, name='dispatch')
class CustomLoginView(View):
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user:
            login(request, user)

            # Create the response
            response = JsonResponse({'message': 'Login successful'}, status=200)

            # Set the session cookie explicitly
            response.set_cookie(
                'sessionid',
                value=request.session.session_key,  # Use Django's session key
                max_age=1209600,  # 2 weeks
                httponly=True,  # Prevent JavaScript access to the cookie
                secure=False,    # Only send cookie over HTTPS when True (development: False)
                samesite='Lax'  # Prevent cross-origin requests except top-level navigations
            )
            return response
        else:
            return JsonResponse({'error': 'Invalid credentials'}, status=400)