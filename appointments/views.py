from django.shortcuts import render, get_object_or_404, reverse
from django.views.generic import View
from .models import Appointment
from datetime import datetime, timedelta
from django.contrib import messages
from django.http import HttpResponse
from django.http import HttpResponseRedirect
# import Appointment model

# create AppointmentCreateView


class AppointmentCreate(View):

    def get(self, request, *args, **kwargs):
        appointment = None
        return render(request, "appointments.html", {"appointment": appointment})

    def post(self, request, *args, **kwargs):
        service = request.POST.get('service')
        day = request.POST.get('day')
        #Storing day and service in django session
        request.session['service'] = service
        request.session['day'] = day

        appointment = Appointment(service=service, day=day)
        appointment.save()






    # template_name = 'appointments.html'



    # def get(self, request, *args, **kwargs):
    #     # queryset = Appointment.objects.filter()
    #     # appointment = get_object_or_404(queryset)
    #     appointment = """<h1>welcome to my page</h1>"""
    #     return render(
    #         request,
    #         "appointments.html",
    #         {"appointment": appointment})


