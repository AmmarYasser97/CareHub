from django.db import models

class Patient(models.Model):
    name=models.CharField()
    sex=models.CharField()
    age=models.PositiveInetgerField()
    medicalRecord=models.SlugField()
    
