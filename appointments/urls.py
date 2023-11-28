from . import views
from django.urls import path
from appointments.views import Appointment

urlpatterns = [
    path('add_appointment/', views.add_appointment, name='add_appointment'),
    path('view_appointment/', views.view_appointment, name='view_appointment'),
    path('edit/<int:appointment_id>', views.edit_appointment,
         name='edit_appointment'),
    path('delete/<int:appointment_id>', views.delete_appointment,
         name='delete_appointment'),
]
