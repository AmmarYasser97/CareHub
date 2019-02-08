from django.shortcuts import render, redirect
from . import forms
def clinicslist(request):
    return render(request,'clinics/clinics.html')

def create(request):
    if request.method == 'POST':
        form = forms.CreateService(request.POST)
        if form.is_valid():
            x = form.save(commit=False)
            x.save()
            return redirect('services:cl')

    else:

        form= forms.CreateService()
        return render(request,'clinics/createService.html',{'form':form})
