from rest_framework.routers import DefaultRouter
from api.views import TProvinciaViewSet, TDepartamentoViewSet, TLocalidadViewSet, TBarrioViewSet, TCPCViewSet, TLocalizacionViewSet
from api.views import CustomUserViewSet

router = DefaultRouter()
router.register(r'provincia', TProvinciaViewSet, basename='provincia')
router.register(r'departamento', TDepartamentoViewSet, basename='departamento')
router.register(r'localidad', TLocalidadViewSet, basename='localidad')
router.register(r'barrio', TBarrioViewSet, basename='barrio')
router.register(r'cpc', TCPCViewSet, basename='cpc')
router.register(r'localizacion', TLocalizacionViewSet, basename='localizacion')
router.register(r'user', CustomUserViewSet, basename='user')

urlpatterns = router.urls
