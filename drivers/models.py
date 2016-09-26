from __future__ import unicode_literals

from django.db import models
from locations.models import Location


class Driver(models.Model):
    name = models.CharField(max_length=200, blank=False)
    phone = models.CharField(max_length=200, blank=False)
    fare = models.FloatField(blank=False)
    kilometers_driven = models.FloatField(default=0, blank=True)
    car_type = models.CharField(max_length=200, blank=False)
    car_number = models.CharField(max_length=200, blank=False)
    has_ac = models.BooleanField()
    capacity = models.IntegerField(default=1)
    location = models.ForeignKey(Location)
    number_of_times_fined = models.IntegerField(default=0)
    total_fines = models.FloatField(default=0)
    rating = models.FloatField(default=0)
    created_at = models.DateField()
    modified_at = models.DateField()

    def __str__(self):
        return self.name


