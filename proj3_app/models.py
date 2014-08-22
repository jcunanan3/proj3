from django.db import models

# Create your models here.
class Report(models.Model):
    # Some of these fields could be separate tables possibly or a list of choices?
    # This would make it easier to do any kind of filtering or statistical analysis
    # later on different categories for example.
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

