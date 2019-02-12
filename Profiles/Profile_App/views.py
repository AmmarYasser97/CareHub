from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import loader


def patient(request):
    template = loader.get_template('patient.html')
    context = {


    }
    return HttpResponse(template.render(context, request))