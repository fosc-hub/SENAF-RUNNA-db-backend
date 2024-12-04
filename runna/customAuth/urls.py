from customAuth.views import CustomUserViewSet, CurrentUserView, CustomLoginView, CustomLogoutView
from django.urls import path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'users', CustomUserViewSet, basename='user')

urlpatterns = router.urls + [
    path('user/me/', CurrentUserView.as_view(), name='current-user'),
    
    path('login/', CustomLoginView.as_view(), name='login'),
    
    path('logout/', CustomLogoutView.as_view(), name='custom-logout'),
]