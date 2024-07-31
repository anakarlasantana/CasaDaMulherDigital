from rest_framework import serializers
from ....models import Politics  


class PoliticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Politics
        fields = ['id', 'name', 'description']
