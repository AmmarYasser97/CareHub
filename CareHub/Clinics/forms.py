from django import forms
from . import models

class CreateService(forms.ModelForm):
    class Meta:
        model=models.Service
        fields = ['name','doctors','start_time','end_time','type']