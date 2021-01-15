# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Airport(models.Model):
    ident = models.CharField(max_length=10, blank=True, null=True)
    airport_name = models.CharField(max_length=100, blank=True, null=True)
    continent = models.CharField(max_length=3, blank=True, null=True)
    iso_country = models.CharField(max_length=3, blank=True, null=True)
    iso_region = models.CharField(max_length=3, blank=True, null=True)
    municipality = models.CharField(max_length=40, blank=True, null=True)
    gps_code = models.CharField(max_length=6, blank=True, null=True)
    iata_code = models.CharField(max_length=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Airport'


class Passenger (models.Model):
    adult_pass = (
        ('1', 1),
        ('2', 2),
        ('3', 3),
    )
    adult_passengers = models.CharField(max_length=1, choices=adult_pass)

    child_pass = (
        ('0', 0),
        ('1', 1),
        ('2', 2),
    )
    child_passengers = models.CharField(max_length=1, choices=child_pass)

    # hata  total_passengers = adult_passengers + child_passengers


class Flight (models.Model):
    Travel_Class = (
        ('E', 'Economy Class'),
        ('B', 'Business Class'),
        ('F', 'First Class'),
    )
    travel_class = models.CharField(max_length=1, choices=Travel_Class)
    departing_date = models.DateField()
    returning_date = models.DateField()
    # dolaylı hata passengers = models.ForeignKey(Passenger.total_passengers, on_delete=models.CASCADE)'
    # deptAirport = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='deptAirport')
    # arrAirport = models.ForeignKey(Airport, on_delete=models.SET_DEFAULT, related_name='arrAirport')
    duration = models.DateTimeField()
    airline = models.CharField(max_length=20)
