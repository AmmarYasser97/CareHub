from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import loader
from django.views.generic import UpdateView

from Profile_App.models import Patient


def patient(request):
    template = loader.get_template('patient.html')
    context = {

        'Patient': Patient.objects.get(pk=1),




    }
    return HttpResponse(template.render(context, request))

