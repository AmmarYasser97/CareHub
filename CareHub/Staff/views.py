from .models import Doctor
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView


class DoctorListView(ListView):
    model = Doctor
    #template_name = 'Staff/doctor_list.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'doctors'
    ordering = ['name']


class DoctorDetailView(DetailView):
    model = Doctor


class DoctorCreateView(CreateView):
    model = Doctor
    fields = ['name', 'expertise', 'email', 'rating', 'availability']


class DoctorUpdateView(UpdateView):
    model = Doctor
    fields = ['name', 'expertise', 'email', 'rating', 'availability']
    template_name_suffix = '_update_form'


class DoctorDeleteView(DeleteView):
    model = Doctor
    success_url = '/staff'
