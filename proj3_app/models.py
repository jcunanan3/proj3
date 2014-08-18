from django.db import models

# Create your models here.
class Report(models.Model):
    incident = models.CharField(max_length=100)
    category = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    dayofweek = models.CharField(max_length=12)
    date = models.DateField()
    time = models.TimeField()
    precinct = models.CharField(max_length=50)
    resolution = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    lat = models.FloatField()
    long = models.FloatField()

class Crime_Report(models.Model):
    incident = models.CharField(max_length=20)
    category = models.CharField(max_length=30)
    description = models.CharField(max_length=50)
    dayofweek = models.CharField(max_length=12)
    date = models.DateField()
    time = models.TimeField()
    precinct = models.CharField(max_length=20)
    resolution = models.TextField(max_length=200)
    location = models.CharField(max_length=40)
    lat = models.FloatField()
    long = models.FloatField()