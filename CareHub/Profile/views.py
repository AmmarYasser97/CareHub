from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.views.generic import UpdateView
from .models import Patient
from Clinics.models import Reservation
from django.shortcuts import redirect


def patient(request, name):
    template = loader.get_template('patient.html')
    

    Reservations = []
    Reservations.extend(Reservation.rManager.filter(Booker=Patient.getter.get(pk=name).user))

    context = {

        'Patient': Patient.getter.get(pk=name),
        'Reservations': Reservations




    }
    return HttpResponse(template.render(context, request))


def patient_update(request, name):
    template = loader.get_template('patient-update.html')
    context = {

        'Patient': Patient.getter.get(pk=name),

    }
    return HttpResponse(template.render(context, request))


# to save edit profile data in database
'''
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
'''


def patient_update_form(request):

    template = loader.get_template('patient.html')
    
    context = {
        'Patient': Patient.getter.get(pk=1),
    }

    First_Name = request.POST["FirstName"]
    Last_Name = request.POST["LastName"]
    Email = request.POST["Email"]
    Password = request.POST["Password"]

    Age = request.POST["Age"]
    Blood_Type = request.POST["BloodType"]
    Weight = request.POST["Weight"]
    Height = request.POST["Height"]
    Contact = request.POST["Contact"]

    # Medical History
    Allergies = request.POST["Allergies"]
    Medications = request.POST["Medications"]
    Past_Operations = request.POST["PastOperations"]
    Family_History = request.POST["FamilyHistory"]

    # Additional Info
    if 'Athletic' in request.POST:
        Athletic = True
    else:
        Athletic = False

    if 'Smoker' in request.POST:
        Smoker = True
    else:
        Smoker = False

    if 'OrganDonor' in request.POST:
        Organ_Donor = True
    else:
        Organ_Donor = False

    Patient_Info = Patient.getter.get(pk=3)

    Patient_Info.user.first_name = First_Name
    Patient_Info.user.last_name = Last_Name
    Patient_Info.user.email = Email
    Patient_Info.user.password = Password

    Patient_Info.Athletic = Athletic
    Patient_Info.Smoker = Smoker
    Patient_Info.Family_History = Family_History
    Patient_Info.Past_Operations = Past_Operations
    Patient_Info.Medications = Medications
    Patient_Info.Age = Age
    Patient_Info.Contact = Contact
    Patient_Info.Organ_Donor = Organ_Donor
    Patient_Info.Height = Height
    Patient_Info.Blood_Type = Blood_Type
    Patient_Info.Weight = Weight
    Patient_Info.user.save()
    Patient_Info.save()

    return redirect('profile_page:patient' + name + '/')
