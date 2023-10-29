from django.shortcuts import render, get_object_or_404, reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from .models import Appointment
from datetime import datetime, timedelta
from .forms import AppointmentForm
from django.contrib import messages
from django.http import HttpResponse
from django.http import HttpResponseRedirect
# import Appointment model

# create AppointmentCreateView


@login_required
class AppointmentCreate(View):

    
    def get(self, request):
        if request.method == "POST":
            user = request.POST.get('name')
            service = request.POST.get('service')
            day = request.POST.get('day')
            time = request.POST.get('time')
            request.session['user'] = name
            request.session['service'] = service
            request.session['day'] = day
            request.session['time'] = time

        return render(request, 'appointments.html',
        {
            "appointment_form": AppointmentForm(),
            "booked": False
        })
        





























    # def get(self, request, *args, **kwargs):
    #     appointment = None
    #     return render(request, "appointments.html", {"appointment": appointment})

    # # Get service, day and time submitted via POST request and ensure that
    # # service and day fields are completed
    # def post(self, request, *args, **kwargs):
    #     service = request.POST.get('service')
    #     day = request.POST.get('day')
    #     time = request.POST.get('time')
    #     if service == '' or day == '':
    #         messages.error(request, "Please Select A Service and Date")
    #     #Storing day and service in django session
    #     request.session['service'] = service
    #     request.session['day'] = day
    #     request.session['time'] = time

    #     appointment = Appointment(service=service, day=day)
    #     appointment.save()











    # def get(self, request):
    #     if request.method == "POST":
    #         user = request.POST.get('name')
    #         service = request.POST.get('service')
    #         day = request.POST.get('day')
    #         time = request.POST.get('time')
    #         return render(request, 'edit_booking.html', {})

    #     else:
    #         return render(request, 'appointments.html', {})

    # def post()


# class EdditBooking(SuccessMessageMixin, UpdateView):
#     model = Appointment
#     template_name = edit-booking.html
#     fields = ['service', 'day', 'time']






    # template_name = 'appointments.html'
