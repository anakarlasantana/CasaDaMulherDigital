from rest_framework import serializers
from ....models import Politices  


class PoliticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Politices
        fields = ['id', 'name', 'description']
