# admin.py in the same app where your models.py is located

# Importing necessary modules from Django's admin and the model you've created.
from django.contrib import admin
from .models import Appointment

# Creating a custom admin class for the Appointment model.


class AppointmentAdmin(admin.ModelAdmin):

    # `list_display` specifies which fields from the model should be displayed on the main admin list page.
    list_display = ('user', 'service', 'day', 'time', 'time_ordered')

    # `list_filter` adds a sidebar on the right that allows filtering the displayed results by these fields.
    list_filter = ('service', 'day', 'time')

    # `search_fields` determines which fields will be searched when using the search box in the admin interface.
    # The notation 'user__username' indicates searching in the 'username' field of the related 'user' model.
    search_fields = ('user__username', 'service', 'day')

    # `ordering` sets the default ordering for the list display.
    # Here, '-time_ordered' means it will order by the 'time_ordered' field in descending order.
    ordering = ['-time_ordered']


# Registering the Appointment model with the admin site using the custom admin class.
admin.site.register(Appointment, AppointmentAdmin)
