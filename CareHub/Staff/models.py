from django.db import models
from django.core.validators import MaxValueValidator
from django.urls import reverse


class Doctor(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics', null=True)
    expertise = models.CharField(max_length=50)
    email = models.EmailField(max_length=70, null=False, unique=True)
    rating = models.PositiveSmallIntegerField(validators=[MaxValueValidator(5)])
    availability = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('staff-detail', kwargs={'pk': self.pk})
