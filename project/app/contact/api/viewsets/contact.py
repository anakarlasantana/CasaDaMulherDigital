from rest_framework import viewsets
from app.models import Contact
from app.contact.api.serializers.contact import ContactSerializer


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
