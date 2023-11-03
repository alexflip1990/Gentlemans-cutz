from .models import Appointment
from django import forms


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['service', 'day', 'time']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['service'].required = True
        self.fields['day'].required = True
        self.fields['time'].required = True
