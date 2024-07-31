from rest_framework import serializers
from app.models import Contact


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'name', 'message', 'email', 'phone']
