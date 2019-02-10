from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Patient(models.Model):
    Op = 'O Positive'
    On = 'O Negative'
    Ap = 'A Positive'
    An = 'A Negative'
    Bp = 'B Positive'
    Bn = 'B Negative'
    ABp = 'AB Positive'
    ABn = 'AB Negative'

    Blood_Types = ((Op, 'O+'),(On,'O-'),(Ap,'A+'),(An,'A-'),(Bp,'B+'),(Bn,'B-'),(ABp,'AB+'),(ABn,'AB-')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image =  models.ImageField(default='defaultPatient.jpg',upload_to='patient_profile_pics')
    Age = models.PositiveSmallIntegerField()
    Blood_Type =models.CharField(max_length=11,choices=Blood_Types, default= Ap)
    Weight =models.PositiveSmallIntegerField()
    Height =models.PositiveSmallIntegerField()
    Emergency_Contact =models.BigIntegerField()

def __str__(self):
        return f'{self.user.username} Patient'
