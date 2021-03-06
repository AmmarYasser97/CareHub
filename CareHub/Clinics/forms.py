from django import forms
from . import models


class CreateService(forms.ModelForm):
    class Meta:
        model = models.Service
        fields = ['name', 'doctors', 'start_time', 'end_time', 'type']


class Book(forms.ModelForm):
    class Meta:
        model = models.Reservation
        
        fields = ['Clinic', 'Doctor']
        labels = {'Clinic': ('Service'),}


class BookR(forms.ModelForm):
    class Meta:
        model = models.Reservation
        fields = ['Clinic', 'Doctor', 'Patient']
        labels = {'Clinic': ('Service'),}
