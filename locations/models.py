from __future__ import unicode_literals

from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=200, blank=False, unique=True)
    create_at = models.DateField()
    modified_at = models.DateField()

    def __str__(self):
        return self.name


class LocationDistances(models.Model):
    from_place = models.ForeignKey(Location, blank=False, related_name='from_place')
    to_place = models.ForeignKey(Location, blank=False, related_name='to_place')
    distance = models.FloatField(blank=False)
    create_at = models.DateField()
    modified_at = models.DateField()
