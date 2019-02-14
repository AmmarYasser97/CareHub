from django import forms

class RegisterForm(forms.Form):
    Op = 'O Positive'
    On = 'O Negative'
    Ap = 'A Positive'
    An = 'A Negative'
    Bp = 'B Positive'
    Bn = 'B Negative'
    ABp = 'AB Positive'
    ABn = 'AB Negative'

    Blood_Types = ((Op, 'O+'), (On, 'O-'), (Ap, 'A+'), (An, 'A-'), (Bp, 'B+'), (Bn, 'B-'), (ABp, 'AB+'), (ABn, 'AB-'))

    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password_repeat = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    Age = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control'}), max_value = 100)
    Height = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control'}), max_value = 250)
    Weight = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control'}), max_value = 200)
    Blood_Type = forms.ChoiceField(choices = Blood_Types, widget=forms.Select(attrs={'class':'form-control'}))
    Contact = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), max_length=10, min_length=10)

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
