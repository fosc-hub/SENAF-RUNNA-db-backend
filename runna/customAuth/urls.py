from customAuth.views import EquipoViewSet ,CustomUserViewSet, CurrentUserView
from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

router = DefaultRouter()

router.register(r'equipo', EquipoViewSet, basename='equipo')
router.register(r'users', CustomUserViewSet, basename='user')

urlpatterns = router.urls + [
    path('user/me/', CurrentUserView.as_view(), name='current-user'),
    
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),

]