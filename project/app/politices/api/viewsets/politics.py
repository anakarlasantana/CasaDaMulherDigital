from rest_framework import viewsets, filters
from app.models import Politices
from app.politices.api.serializers.politics import PoliticsSerializer
from app.filters import PoliticesFilter

class PoliticsViewSet(viewsets.ModelViewSet):
    queryset = Politices.objects.all()
    serializer_class = PoliticsSerializer
    filterset_class = PoliticesFilter
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)  
