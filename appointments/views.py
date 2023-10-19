from django.shortcuts import render, get_object_or_404, reverse
from django.views.generic import View
from .models import Appointment
from django.http import HttpResponse
from django.http import HttpResponseRedirect
# import Appointment model

# create AppointmentCreateView


class AppointmentCreate(View):

    # template_name = 'appointments.html'

    # def get_context_data(self, slug, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['appointments'] = self.request.user.appointment_set.all()
    #     return HttpResponseRedirect(reverse('appointments', args=[slug]))

    def get(self, request, *args, **kwargs):
        # queryset = Appointment.objects.filter()
        # appointment = get_object_or_404(queryset)
        appointment = """<h1>welcome to my page</h1>"""
        return render(
            request,
            "appointments.html",
            {"appointment": appointment})

# 'referring to PostDetail
# def get()
#   render that template you created
