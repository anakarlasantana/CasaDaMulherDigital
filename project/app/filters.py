# filters.py
import django_filters
from .models import Services, Units, Politices

class ServicesFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    
    class Meta:
        model = Services
        fields = ['name', 'description']

class UnitsFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    
    class Meta:
        model = Units
        fields = ['name', 'email']

class PoliticesFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    
    class Meta:
        model = Politices
        fields = ['name', 'description']

