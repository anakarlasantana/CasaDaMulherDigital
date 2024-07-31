from rest_framework import viewsets
from app.models import Units  
from app.units.api.serializers.units import UnitsSerializer  


class UnitsViewSet(viewsets.ModelViewSet):
    queryset = Units.objects.all()
    serializer_class = UnitsSerializer
