from django.shortcuts import render, get_object_or_404, reverse
from django.views.generic import View
from .models import Appointment
from datetime import datetime, timedelta
# from .forms import BookingForm
from django.contrib import messages
from django.http import HttpResponse
from django.http import HttpResponseRedirect
# import Appointment model

# create AppointmentCreateView


class AppointmentCreate(View):

    def get(self, request, *args, **kwargs):
        appointment = None
        return render(request, "appointments.html", {"appointment": appointment})

    # Get service, day and time submitted via POST request and ensure that
    # service and day fields are completed
    def post(self, request, *args, **kwargs):
        service = request.POST.get('service')
        day = request.POST.get('day')
        time = request.POST.get('time')
        if service == '' or day == '':
            messages.error(request, "Please Select A Service and Date")
        #Storing day and service in django session
        request.session['service'] = service
        request.session['day'] = day
        request.session['time'] = time

        appointment = Appointment(service=service, day=day)
        appointment.save()


# class EdditBooking(SuccessMessageMixin, UpdateView):
#     model = Appointment
#     template_name = edit-booking.html
#     fields = ['service', 'day', 'time']






    # template_name = 'appointments.html'
