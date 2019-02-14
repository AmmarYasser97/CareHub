from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password_repeat = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    Age = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control'}))
    Height = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control'}))
    Weight = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control'}))
    Blood_Type = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    Contact = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control'}))

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
