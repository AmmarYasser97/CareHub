from django import forms
from .import models


class ProfileEdit(forms.ModelForm):
    class Meta:
        model = models.Patient
        fields = ['name', 'age', 'blood', 'height', 'weight', 'Emergency', 'email', 'contact', 'Organ_Donor', 'Allergies', 'Athletic', 'Operation', 'Meds', 'Smoker', 'History']
