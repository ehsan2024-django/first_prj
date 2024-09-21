from django.db import models

# Create your models here.
class City(models.Model):
    city_name = models.CharField(max_length=100)
    city_lat = models.FloatField(max_length=100, default=35.78)
    city_long = models.FloatField(max_length=100, default=35.78)