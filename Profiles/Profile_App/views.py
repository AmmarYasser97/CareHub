from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import loader
from django.views.generic import UpdateView

from Profile_App.models import Patient


def patient(request):
    template = loader.get_template('patient.html')
    context = {

        'Patient': Patient.objects.get(pk=3),




    }
    return HttpResponse(template.render(context, request))


# to save edit profile data in database

def profile_edit(request):
    if request.method == 'POST':
        form = forms.ProfileEdit(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.patient = request.user
            instance.save()
            return redirect('profile')
        else:
            form = forms.ProfileEdit()
    else:
        form = forms.ProfileEdit()
    return render(request, 'patient-update.html', {'forms': form})
