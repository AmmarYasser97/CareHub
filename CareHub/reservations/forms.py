from django import forms
from . import models


class Book(forms.ModelForm):
    class Meta:
        model = models.Reservation
        fields = ['Clinic','Doctor']
