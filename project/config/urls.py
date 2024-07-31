from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app.politices.api.viewsets.politics import PoliticsViewSet
from app.contact.api.viewsets.contact import ContactViewSet
from app.services.api.viewsets.services import ServicesViewSet
from app.units.api.viewsets.units import UnitsViewSet
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,  
)

router = DefaultRouter()
router.register(r'politices', PoliticsViewSet)
router.register(r'contacts', ContactViewSet)  
router.register(r'services', ServicesViewSet)
router.register(r'units', UnitsViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path(
        'api/docs/swagger-ui/',
        SpectacularSwaggerView.as_view(url_name='schema'),
        name='swagger-ui'
    ),
    path(
        'api/docs/redoc/',
        SpectacularRedocView.as_view(url_name='schema'),
        name='redoc'
    ),
]
