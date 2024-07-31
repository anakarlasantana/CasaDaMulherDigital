from rest_framework import viewsets
from app.models import Services  
from ..serializers.services import ServiceSerializer  


class ServicesViewSet(viewsets.ModelViewSet):
    queryset = Services.objects.all()
    serializer_class = ServiceSerializer
