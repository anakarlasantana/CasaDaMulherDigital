from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app.policies.api.viewsets.politics import PoliticsViewSet

router = DefaultRouter()
router.register(r'politics', PoliticsViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
