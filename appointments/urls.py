from . import views
from django.urls import path
from appointments.views import Appointment

urlpatterns = [
    path('appointments/', views.appointments, name='appointments'),
    path('add_appointment/', views.add_appointment, name='add_appointment'),
    path('view_appointment/', views.view_appointment, name='view_appointment'),
    path('edit/<appointment_id>', views.edit_appointment, name='edit_appointment'),
    path('delete/<appointment_id>', views.delete_appointment, name='delete_appointment'),
]

