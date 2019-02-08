from django.db import models
from Staff.models import Doctor
from django.urls import reverse
from django.contrib.auth.models import User


class Service(models.Model):
    '''
    NOTE:
    this model is for both clinic and scan to save a lot of duplicate code and tables in database
    according to that approach the models.py of Scans application will be empty
    '''

    name = models.CharField(max_length=50)
    start_time = models.TimeField(auto_now=False, auto_now_add=False)
    end_time = models.TimeField(auto_now=False, auto_now_add=False)
    no_appointments = models.PositiveSmallIntegerField(default=0)
    type = models.CharField(max_length=1)
    # type = 'C' for CLINIC or type = 'S' for SCAN
    doctors = models.ManyToManyField(Doctor)
    availability = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('service-detail', kwargs={'pk': self.pk})


class Reservation(models.Model):
    Clinic = models.ForeignKey(Service, on_delete=models.CASCADE, default=None)
    Doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    Patient = models.ForeignKey(User, on_delete=models.CASCADE)
    Time = models.TimeField(auto_now=False, auto_now_add=False)
    DateOfBook = models.DateField(auto_now_add=True)
    

    def __str__(self):
        return self.Clinic.name

    def get_absolute_url(self):
        return reverse('service-list', kwargs={'pk': self.pk})
