from django.conf import settings
from django.db import models
from django.utils import timezone

class TravelOption(models.Model):
    TYPE_CHOICES = [
        ('flight', 'Flight'),
        ('train', 'Train'),
        ('bus', 'Bus'),
    ]

    travel_id = models.CharField(max_length=20, unique=True)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    source = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    departure = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available_seats = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['departure']

    def __str__(self):
        return f"{self.get_type_display()} {self.travel_id}: {self.source} → {self.destination} ({self.departure:%Y-%m-%d %H:%M})"


class Booking(models.Model):
    STATUS_CHOICES = [
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    travel_option = models.ForeignKey(TravelOption, on_delete=models.PROTECT)
    seats = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=12, decimal_places=2)
    booking_date = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='confirmed')

    class Meta:
        ordering = ['-booking_date']

    def __str__(self):
        return f"Booking #{self.pk} - {self.user} - {self.travel_option}"
