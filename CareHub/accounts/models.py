from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Patient(models.Model):
    name = models.CharField(max_length=250, default=None)
    age = models.IntegerField(default=None)
    blood = models.CharField(max_length=3, default=None)
    weight = models.IntegerField(default=None)
    height = models.IntegerField(default=None)
    Emergency = models.IntegerField(default=0)
    Organ_Donor = models.CharField(max_length=3, default=None)
    Allergies = models.TextField(default=None)
    Meds = models.TextField(default=None)
    Operation = models.TextField(default=None)
    History = models.TextField(default=None)
    contact = models.IntegerField(default=None)
    Smoker = models.CharField(max_length=3, default=None)
    Athletic = models.CharField(max_length=3, default=None)
    email = models.CharField(max_length=250, default=None)
    this = models.ForeignKey(User, on_delete=models.CASCADE, default=None)


