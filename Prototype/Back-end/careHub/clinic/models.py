from django.db import models

class Clinic(models.Model):
    name=models.CharField()
    doctors=models.SlugField()
    availability=models.BooleanField()