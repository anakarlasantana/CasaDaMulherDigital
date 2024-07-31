from rest_framework import viewsets
from ....models import Politics  
from ..serializers.politics import PoliticsSerializer  


class PoliticsViewSet(viewsets.ModelViewSet):
    queryset = Politics.objects.all()
    serializer_class = PoliticsSerializer
