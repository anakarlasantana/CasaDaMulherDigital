from rest_framework import serializers
from app.models import Units


class UnitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Units
        fields = '__all__'