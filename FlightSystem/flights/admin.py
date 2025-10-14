from django.contrib import admin
from .models import AirportRoute

@admin.register(AirportRoute)
class AirportRouteAdmin(admin.ModelAdmin):
    list_display = ('airport_code', 'position', 'duration')
    search_fields = ('airport_code',)
