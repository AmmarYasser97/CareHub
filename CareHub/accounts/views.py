from django.contrib.auth.models import User, Group
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import RegisterForm, LoginForm
from django.shortcuts import redirect
from Profile.models import Patient
from Profile.views import patient

def is_receptionist(user):
    return user.groups.filter(name='Receptionist').exists()

def Receptionist (request):
    return render(request, 'accounts/receptionist.html')

def profile (request):
    name = str(Patient.getter.get(user=request.user).pk)
    return patient(request,name)

def SignUp (request):
            # if this is a POST request we need to process the form data
    template = 'accounts/signUP.html'

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RegisterForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            if User.objects.filter(username=form.cleaned_data['username']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'Username already exists.'
                })
            elif User.objects.filter(email=form.cleaned_data['email']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'Email already exists.'
                })
            elif form.cleaned_data['password'] != form.cleaned_data['password_repeat']:
                return render(request, template, {
                    'form': form,
                    'error_message': 'Passwords do not match.'
                })
            else:
                # Create the user:
                user = User.objects.create_user(
                    form.cleaned_data['username'],
                    form.cleaned_data['email'],
                    form.cleaned_data['password']
                )
                user.first_name = form.cleaned_data['first_name']
                user.last_name = form.cleaned_data['last_name']
                user.save()

                p = Patient(user=user, Age=request.POST['Age'], Blood_Type=request.POST['Blood_Type'], Weight=request.POST['Weight'], Height=request.POST['Height'], Contact=request.POST['Contact'] )
                p.save()


                # Login the user
                login(request, user)

                # redirect to accounts page:
                name = str(Patient.getter.get(user=request.user).pk)
                return patient(request,name)

   # No post data availabe, let's just show the page.
    else:
        form = RegisterForm()

    return render(request, template, {'form': form})

def SignIn (request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if (user is not None and is_receptionist(user)):
                login(request, user)
                return redirect ('accounts:receptionist')
            elif user is not None:
                login(request, user)
                name = str(Patient.getter.get(user=request.user).pk)
                return patient(request,name)

            else:
                return render (request, 'accounts/signIN.html',{'form':form, 'error_message':'username or password is incorrect'})
    else:
        form = LoginForm()
    return render (request, 'accounts/signIN.html',{'form':form})

def SignOut (request):
    logout(request)
    return render (request, 'index.html')
