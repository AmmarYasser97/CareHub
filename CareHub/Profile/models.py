from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class Patient(models.Model):
    getter = models.Manager()
    Op = 'O Positive'
    On = 'O Negative'
    Ap = 'A Positive'
    An = 'A Negative'
    Bp = 'B Positive'
    Bn = 'B Negative'
    ABp = 'AB Positive'
    ABn = 'AB Negative'

    Blood_Types = ((Op, 'O+'), (On, 'O-'), (Ap, 'A+'), (An, 'A-'), (Bp, 'B+'), (Bn, 'B-'), (ABp, 'AB+'), (ABn, 'AB-')
                   )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='defaultPatient.jpg', upload_to='patient_profile_pics')

    # tkmlet User

    # Basic Info
    Age = models.PositiveSmallIntegerField()
    Blood_Type = models.CharField(
        max_length=11, choices=Blood_Types, default=Ap)
    Weight = models.PositiveSmallIntegerField()
    Height = models.PositiveSmallIntegerField()
    Contact = models.BigIntegerField()

    # Medical History
    Allergies = models.TextField(default="None")
    Organ_Donor = models.BooleanField(default=False)
    Medications = models.TextField(default="None")
    Past_Operations = models.TextField(default="None")
    Family_History = models.TextField(default="None")

    # Additional Info
    Athletic = models.BooleanField(default=False)
    Smoker = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username}'

    def get_absolute_url(self):
        return reverse('Profile:patient', kwargs={'name': self.pk})
