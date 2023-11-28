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


"""
Add a new appointment for logged-in user

This view based function will handle the creation of a new appointment.
It will check for the specified date and time chosen to see if an appointment
with that information already exists. If an existing appointment is found, it
will display an error message. If no previous appointment exists the new
appointment is saved to the database assoiciated with the logged-in user and a
success message is displayed.
"""


@ login_required
def add_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.user = request.user
            appointment_time = appointment.time
            appointment_date = appointment.date
            exist_appointment = (Appointment.objects.filter
                                 (time=appointment_time, date=appointment_date)
                                 .first())
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


"""
Display a list of appointments for the logged-in user

This view based function retrieves a list of appointments associated with the
logged-in user from the database and renders the 'view_appointment.html'
template to display them.
"""


@login_required
def view_appointment(request):
    appointment = Appointment.objects.filter(user=request.user)
    context = {
        'appointment': appointment
    }
    return render(request, 'view_appointment.html', context)


"""
Edit an existing appointment

This view based function allows the logged-in user to edit their existing
appointments identified by the 'appointment_id'. If the request method is POST
and the form is valid, the appointment details are updated to the database. A
success message is displayed and the user is redirected to the
'view_appointment' page
"""


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


"""
Delete an existing appointment

This view based function allows the logged-in user to delete their appointments
identified by the 'appointment_id'. If the request method is POST, the
appointment is deleted from the database and a success message is displayed.
The user is then redirected to the 'add_appointment' page.
"""


@login_required
def delete_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    if request.method == 'POST':
        appointment.delete()
        messages.success(request, 'Your appointment has been deleted.')
        return redirect('add_appointment')
    else:
        return render(request, 'delete_appointment.html',
                      {'appointment': appointment})
