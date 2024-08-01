from rest_framework import viewsets, filters
from app.models import Services  
from ..serializers.services import ServiceSerializer  
from app.filters import ServicesFilter


class ServicesViewSet(viewsets.ModelViewSet):
    queryset = Services.objects.all()
    serializer_class = ServiceSerializer
    filterset_class = ServicesFilter
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)  