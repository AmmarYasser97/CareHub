from django.db import models
from django.core.validators import MaxValueValidator


class Doctor(models.Model):
    name = models.CharField(max_length=50)
    #image = models.ImageField(upload_to=None, height_field=300, width_field=300,null=True)
    expertise = models.CharField(max_length=50)
    email = models.EmailField(max_length=70, blank=True, null=False, unique=True)
    rating = models.PositiveSmallIntegerField(validators=[MaxValueValidator(5)])
    availability = models.BooleanField(default=False)

    def __str__(self):
        return self.name
