from django.db import models
from Staff.models import Doctor

'''
NOTE:
this model is for both clinic and scan to save a lot of duplicate code and tables in database
according to that approach the models.py of Scans application will be empty
'''


class Service(models.Model):
    name = models.CharField(max_length=50)
    start_time = models.TimeField(auto_now=False, auto_now_add=False)
    end_time = models.TimeField(auto_now=False, auto_now_add=False)
    no_appointments = models.PositiveSmallIntegerField()
    type = models.CharField(max_length=1)
    # type = 'C' for CLINIC or type = 'S' for SCAN
    doctors = models.ManyToManyField(Doctor)
    availability = models.BooleanField(default=False)

    def __str__(self):
        return self.name
