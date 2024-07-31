from django.contrib import admin
from app.models import Politices
from app.models import Contact
from app.models import Services
from app.models import Units


@admin.register(Politices)
class PoliciesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'data')
    search_fields = ('name',)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'message')
    search_fields = ('name',)


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'get_units_display')
    search_fields = ('name',)

    def get_units_display(self, obj):
        return ", ".join([unit.name for unit in obj.units.all()])
    get_units_display.short_description = 'Units'


@admin.register(Units)
class UnitsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'address', 'email', 'phone')
    search_fields = ('name',)