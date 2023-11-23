from django.contrib.admin import ModelAdmin
from django.contrib import admin
from .models import Appointment


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):

    list_display = ('user', 'service', 'date', 'time', 'time_ordered')

    list_filter = ('service', 'date', 'time')

    search_fields = ['user__username', 'service', 'date']

    ordering = ['-time_ordered']
