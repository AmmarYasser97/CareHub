from .models import Doctor
from django.contrib.auth.models import User, Group
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView


def is_receptionist(user):
    return user.groups.filter(name='Receptionist').exists()

class DoctorListView(ListView):
    model = Doctor
    #template_name = 'Staff/doctor_list.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'doctors'
    ordering = ['name']

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        #context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        Title = 'Doctors'
        
        return {'doctors': Doctor.objects.all(), 'Title': Title}


class DoctorDetailView(DetailView):
    model = Doctor

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        #model = Doctor
        Title = 'Doctor'
        context['Title'] = Title
        return context


class DoctorCreateView(CreateView):
    model = Doctor
    fields = ['name', 'expertise', 'email', 'rating', 'availability']


class DoctorUpdateView(UpdateView):
    model = Doctor
    fields = ['name', 'expertise', 'email', 'availability']
    template_name_suffix = '_update_form'


class DoctorDeleteView(DeleteView):
    model = Doctor
    success_url = '/staff'
