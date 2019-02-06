from django.db import models
from django.core.validators import MaxValueValidator


class Doctor(models.Model):
    name = models.CharField(max_length=50)
    expertise = models.CharField(max_length=50)
    email = models.EmailField(max_length=70, blank=True, null=False, unique=True)
    clinic = models.ForeignKey('Clinics.Service', null=True, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(validators=[MaxValueValidator(5)])
    availability = models.BooleanField(default=False)

    def __str__(self):
        return self.name
