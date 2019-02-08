from django.shortcuts import render, redirect
from . import forms
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from .models import Service


class ServiceListView(ListView):
    model = Service
    context_object_name = 'Services'
    ordering = ['name']


class ServiceDetailView(DetailView):
    model = Service


class ServiceCreateView(CreateView):
    model = Service
    fields = ['name', 'type','start_time','end_time','doctors','availability']


class ServiceUpdateView(UpdateView):
    model = Service
    fields = ['name', 'type','start_time','end_time','doctors','availability']
    template_name_suffix = '_update_form'


class ServiceDeleteView(DeleteView):
    model = Service
    success_url = '/clinics'

def book(request):
    if request.method == 'POST':
        form = forms.Book(request.POST)
        if form.is_valid():
            x = form.save(commit=False)
            x.Patient = request.user
            x.save()
            return redirect('services:cl')

    else:
        form = forms.Book()
    return render(request, 'book/book.html', {'form': form})
