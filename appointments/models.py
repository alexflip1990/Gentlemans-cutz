from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


SERVICE_CHOICES = (

    ("Classic Cut", "Classic cut"),
    ("Cut & Beard", "Cut & Beard"),
    ("Skin Fade", "Skin Fade"),
    ("Skin & Beard", "Skin & Beard"),
    ("Buzz Cut", "Buzz Cut"),
)

TIME_CHOICES = (

    ("9 AM", "9 AM"),
    ("10 AM", "10 AM"),
    ("11 AM", "11 AM"),
    ("1 PM", "1 PM"),
    ("2 PM", "2 PM"),
    ("3 PM", "3 PM"),
    ("4 PM", "4 PM"),
    ("5 PM", "5 PM"),
)


class Appointment(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE)
    service = models.CharField(
        max_length=50, choices=SERVICE_CHOICES, default="Classic Cut")
    date = models.DateField(default=datetime.now)
    time = models.CharField(
        max_length=10, choices=TIME_CHOICES, default="9 AM")
    time_ordered = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return f"{self.user} | day: {self.date} | time: {self.time}"
