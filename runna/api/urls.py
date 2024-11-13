from rest_framework.routers import DefaultRouter
from api.views import (
    CustomUserViewSet, TProvinciaViewSet, TDepartamentoViewSet, TLocalidadViewSet, TBarrioViewSet, TCPCViewSet,
    TLocalizacionViewSet , TVinculoUsuarioLineaViewSet, TInstitucionUsuarioLineaViewSet, TCargoViewSet
    , TResponsableViewSet, TUsuarioLineaViewSet
)

router = DefaultRouter()
router.register(r'user', CustomUserViewSet, basename='user')
router.register(r'provincias', TProvinciaViewSet, basename='provincias')
router.register(r'departamentos', TDepartamentoViewSet, basename='departamentos')
router.register(r'localidades', TLocalidadViewSet, basename='localidades')
router.register(r'barrios', TBarrioViewSet, basename='vulneracion')
router.register(r'cpc', TCPCViewSet, basename='cpc')
router.register(r'localizacion', TLocalizacionViewSet, basename='localizacion')
router.register(r'vinculo-usuario-linea', TVinculoUsuarioLineaViewSet, basename='vinculo-usuario-linea')
router.register(r'institucion-usuario-linea', TInstitucionUsuarioLineaViewSet, basename='institucion-usuario-linea')
router.register(r'cargo', TCargoViewSet, basename='cargo')
router.register(r'responsable', TResponsableViewSet, basename='responsable')
router.register(r'usuario-linea', TUsuarioLineaViewSet, basename='usuario-linea')

urlpatterns = router.urls
