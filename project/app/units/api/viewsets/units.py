from rest_framework import viewsets, filters
from app.models import Units  
from app.units.api.serializers.units import UnitsSerializer  
from app.filters import UnitsFilter

class UnitsViewSet(viewsets.ModelViewSet):
    queryset = Units.objects.all()
    serializer_class = UnitsSerializer
    filterset_class = UnitsFilter
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)  