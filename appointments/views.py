from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from .models import Appointment
from datetime import datetime, timedelta
from .forms import AppointmentForm
from django.contrib import messages
from django.http import HttpResponse
from django.http import HttpResponseRedirect


# Function that allows user to view homepage
# GET
def home(request):
    return render(request, 'gentlemanscutz/base.html')


# Function that allows the user to view blog page
# GET
def blog(request):
    return render(request, 'gentlemanscutz/blog.html')


# Function that allows the user to view appointment page
# GET
def appointments(request):
    return render(request, 'gentlemanscutz/appointments.html')


# Function that allows the user to make an appointment which
# will then add it to the database
@ login_required
def add_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save()
            appointment.user = request.user
            appointment.save()
            messages.success(request, 'Appointment booked!.')
            return redirect('view_appointment')

    form = AppointmentForm()
    context = {
        'form': form
    }
    return render(request, 'gentlemanscutz/appointments.html', context)


# Function that lets the user view their appointment
@login_required
def view_appointment(request):
    appointment = Appointment.objects.filter(user=request.user)
    context = {
        'appointment': appointment
    }
    return render(request, 'gentlemanscutz/view_appointment.html', context)