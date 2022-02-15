from django.contrib import admin
from . models import Event, EventAttendance

# Register your models here.

class EventAdmin(admin.ModelAdmin):
    list_display = ['create_date', 'title', 'event_date', 'event_creator','is_still_active']
    list_per_page = 50
admin.site.register(Event,EventAdmin)

class EventAttendanceAdmin(admin.ModelAdmin):
    list_display = ['event', 'user','id']
    list_per_page = 50
admin.site.register(EventAttendance,EventAttendanceAdmin)
