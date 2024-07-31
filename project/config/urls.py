from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app.politices.api.viewsets.politics import PoliticsViewSet
from app.contact.viewsets.contact import ContactViewSet
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,  # Importação adicionada
)

router = DefaultRouter()
router.register(r'politices', PoliticsViewSet)
router.register(r'contacts', ContactViewSet)  # Corrigido para o ContactViewSet

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
