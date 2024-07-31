from rest_framework import viewsets
from app.models import Politices  
from app.politices.api.serializers.politics import PoliticsSerializer  


class PoliticsViewSet(viewsets.ModelViewSet):
    queryset = Politices.objects.all()
    serializer_class = PoliticsSerializer
