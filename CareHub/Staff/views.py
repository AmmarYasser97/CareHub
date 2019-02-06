from django.shortcuts import render
from .models import Doctor
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


class DoctorListView(ListView):
    model = Doctor
    context_object_name = 'doctors'
    ordering = ['name']


class DoctorDetailView(DetailView):
    model = Doctor
