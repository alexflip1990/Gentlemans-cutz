from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from .models import Appointment
from datetime import datetime, timedelta
from .forms import AppointmentForm
from django.contrib import messages
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db import models
import pdb



# Function that allows user to view homepage
# GET
def home(request):
    return render(request, 'appointments/base.html')


# Function that allows the user to view blog page
# GET
def blog(request):
    return render(request, 'blog/blog.html')


# Function that allows the user to view appointment page
# GET
def appointments(request):
    return render(request, 'appointments.html')


# Function that allows the user to view view_appointment page
# GET
def view(request):
    return render(request, 'view_appointment.html')


# Function that allows the user to view edit_appointment page
# GET
def edit(request):
    return render(request, 'edit_appointment.html')


# Function that allows the user to view delete_appointment page
# GET
def delete(request):
    return render(request, 'delete_appointment.html')


# Function that allows the user to make an appointment which
# will check if an appointment for that date and time already exists
# if so an error message is thrown, if not the appointment is saved to
# the database
@ login_required
def add_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.user = request.user
            appointment_time = appointment.time
            appointment_day = appointment.day
            exist_appointment = Appointment.objects.filter(time=appointment_time, day=appointment_day).first()
            if exist_appointment:
                messages.error(request, 'An appointment has already been made for this time and date')
            else:
                appointment.save()
                messages.success(request, 'Appointment booked!.')
                return redirect('view_appointment')

    form = AppointmentForm()
    context = {
        'form': form
    }
    return render(request, 'add_appointment.html', context)


# Function that lets the user view their appointment
@login_required
def view_appointment(request):
    appointment = Appointment.objects.filter(user=request.user)
    context = {
        'appointment': appointment
    }
    return render(request, 'view_appointment.html', context)


# Function that lets the user edit their appointment once it's been made
@login_required
def edit_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    if request.method == "POST":
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            appointment = form.save()
            appointment.user = request.user
            appointment.save()
            messages.success(request, 'Your appointment has been amended.')
        return redirect('view_appointment')
    form = AppointmentForm(instance=appointment)
    context = {
        'form': form
    }
    return render(request, 'edit_appointment.html', context)


# Function that lets the user delete their appointment
@login_required
def delete_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    if request.method == 'POST':
        appointment.delete()
        messages.success(request, 'Your appointment has been deleted.')
        return redirect('add_appointment')