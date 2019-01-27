from django.db import models

# Create your models here.

class dispenser(models.Model):
    inventory = models.IntegerField()
    bathroom_name = models.TextField()
    lat = models.DecimalField(max_digits = 9, decimal_places = 6)
    lng = models.DecimalField(max_digits = 9, decimal_places = 6)
    max_inventory = models.IntegerField(default = '10')

# class logging(models.Model):
