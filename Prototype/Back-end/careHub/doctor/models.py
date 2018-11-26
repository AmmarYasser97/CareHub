from django.db import models

class Doctor(models.Model):
    name=models.CharField()
    expertise=models.CharField()
    availability=models.BooleanField()
    rating=models.PositiveIntegerField()