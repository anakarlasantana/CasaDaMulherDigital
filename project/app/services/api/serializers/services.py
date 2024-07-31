from rest_framework import serializers
from app.models import Units
from app.units.api.serializers.units import UnitsSerializer  


class ServiceSerializer(serializers.ModelSerializer):
    units = UnitsSerializer(many=True, read_only=True)

    class Meta:
        model = Units
        fields = '__all__'
