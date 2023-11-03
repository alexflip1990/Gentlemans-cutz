from django.contrib.admin import ModelAdmin
from django.contrib import admin
from .models import Appointment


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
 
    list_display = ('user', 'service', 'day', 'time', 'time_ordered')

    list_filter = ('service', 'day', 'time')

    search_fields = ['user__username', 'service', 'day']

    ordering = ['-time_ordered']
