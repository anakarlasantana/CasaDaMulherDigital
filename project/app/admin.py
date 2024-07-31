from django.contrib import admin
from app.models import Politics


@admin.register(Politics)
class PoliciesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    search_fields = ('name',)
