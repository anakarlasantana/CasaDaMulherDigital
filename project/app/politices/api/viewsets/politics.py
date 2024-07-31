from rest_framework import viewsets
from ....models import Politices  
from ..serializers.politics import PoliticsSerializer  


class PoliticsViewSet(viewsets.ModelViewSet):
    queryset = Politices.objects.all()
    serializer_class = PoliticsSerializer
