from django.shortcuts import render, redirect
from . import forms
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from .models import Service
from django.contrib.auth.models import User, Group
from accounts import views as Aviews
from django.contrib.auth.decorators import login_required

class ServiceListView(ListView):
    model = Service
    context_object_name = 'Services'
    ordering = ['name']


class ClinicListView(ListView):
    model = Service
    context_object_name = 'Services'
    ordering = ['name']
    template_name = 'Clinics/clinic_list.html'


class ScanListView(ListView):
    model = Service
    context_object_name = 'Services'
    ordering = ['name']
    template_name = 'Clinics/scan_list.html'


class ServiceDetailView(DetailView):
    model = Service


class ServiceCreateView(CreateView):
    model = Service
    fields = ['name', 'type', 'start_time',
        'end_time', 'doctors', 'availability']


class ServiceUpdateView(UpdateView):
    model = Service
    fields = ['name', 'type', 'start_time',
        'end_time', 'doctors', 'availability']
    template_name_suffix = '_update_form'


class ServiceDeleteView(DeleteView):
    model = Service
    success_url = '/clinics'

@login_required(login_url="/accounts/signin/")
def book(request):

    if (Aviews.is_receptionist):

        if request.method == 'POST':
            form = forms.Book(request.POST)
            if form.is_valid():
                x = form.save(commit=False)
                x.Booker = request.user
                
                x.save()
                return redirect('service-list')

        else:
            form = forms.BookR()
            return render(request, 'book/book.html', {'form': form})


    else:

        if request.method == 'POST':
                    form = forms.Book(request.POST)
                    if form.is_valid():
                        x = form.save(commit=False)
                        x.Booker = request.user
                        x.Patient = str(request.user.get_username())
                        x.save()
                        return redirect('service-list')

        else:
            form = forms.Book()
            return render(request, 'book/book.html', {'form': form})
