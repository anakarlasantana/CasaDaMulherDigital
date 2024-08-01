from rest_framework import serializers
from app.models import Services
from app.units.api.serializers.units import UnitsSerializer  


class ServiceSerializer(serializers.ModelSerializer):
    units = UnitsSerializer(many=True, read_only=True)

    class Meta:
        model = Services
        fields = ['id', 'name', 'description', 'units']
