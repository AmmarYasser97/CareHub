from django.shortcuts import render, redirect
from .models import Patient
from .import forms


def profile(request):
    username = None
    if request.user.is_authenticated():
        username = request.user
    show = Patient.objects.get(this=username)
    context = {
        'name': show.name,
        'age': show.age,
        'blood': show.blood,
        'weight': show.weight,
        'height': show.height,
        'emergency': show.Emergency,
        'contact': show.contact,
        'donor': show.Organ_Donor,
        'Allergies': show.Allergies,
        'meds': show.Meds,
        'operations': show.Operation,
        'history': show.History,
        'smoker': show.Smoker,
        'athletic': show.Athletic,
        'email': show.email
    }
    return render(request, 'Profile.html', context)


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
    return render(request, 'Profile-edit.html', {'forms': form})
