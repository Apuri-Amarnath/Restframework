from django.db import models
from django.contrib.auth.models import User

class Cab(models.Model):
    cab_number = models.CharField(max_length=20)
    driver_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.cab_number} - {self.driver_name}"

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cab = models.ForeignKey(Cab, on_delete=models.CASCADE)
    pickup_location = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    pickup_time = models.DateTimeField()
    booking_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.cab.cab_number} - {self.pickup_location}"
