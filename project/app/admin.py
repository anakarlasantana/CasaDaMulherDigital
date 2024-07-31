from django.contrib import admin
from app.models import Politices


@admin.register(Politices)
class PoliciesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    search_fields = ('name',)
