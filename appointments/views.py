from django.shortcuts import render
from django.views.generic import View
from .models import Appointment
# import Appointment model

# create AppointmentCreateView


class AppointmentCreate(View):

    template_name = 'appointments.html'

    def get_context_data(self, slug, **kwargs):
        context = super().get_context_data(**kwargs)
        context['appointments'] = self.request.user.appointment_set.all()
        return context

# 'referring to PostDetail
# def get()
#   render that template you created
