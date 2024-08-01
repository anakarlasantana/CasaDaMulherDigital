from rest_framework import serializers
from app.models import Politices  


class PoliticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Politices
        fields = ['id', 'name', 'description', 'data', 'image']
