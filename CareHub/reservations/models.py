from django.db import models
from Clinics.models import Service
from Staff.models import Doctor
from django.contrib.auth.models import User, Group


class Reservation(models.Model):
   Clinic = models.ForeignKey(Service, on_delete=models.CASCADE,default=None)
   Doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
   Patient = models.ForeignKey(User, on_delete=models.CASCADE)
   
   def __str__(self):
        return self.Clinic.name



