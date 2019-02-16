from django.shortcuts import render, redirect
from . import forms
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from .models import Service, Reservation
from django.contrib.auth.models import User, Group
from accounts import views as Aviews
from django.contrib.auth.decorators import login_required

class ServiceListView(ListView):
    model = Service
    context_object_name = 'Services'
    ordering = ['name']

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        Title = 'Services'
        context['Services','Title'] = {Service.objects.all() , Title}
        return {'Services':Service.objects.all(), 'Title':Title}


class ClinicListView(ListView):
    model = Service
    context_object_name = 'Services'
    ordering = ['name']
    template_name = 'Clinics/clinic_list.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        Title = 'Clinics'
        context['Services', 'Title'] = {Service.objects.all(), Title}
        return {'Services': Service.objects.all(), 'Title': Title}
    



class ScanListView(ListView):
    model = Service
    context_object_name = 'Services'
    ordering = ['name']
    template_name = 'Clinics/scan_list.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        Title = 'Scans'
        context['Services', 'Title'] = {Service.objects.all(), Title}
        return {'Services': Service.objects.all(), 'Title': Title}


class ServiceDetailView(DetailView):
    model = Service

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        #model = Service
        Title = 'Services'
        context['Title'] = Title
        return context
    


class ServiceCreateView(CreateView):
    model = Service
    fields = ['name', 'type', 'start_time',
        'end_time', 'doctors', 'availability']


class ServiceUpdateView(UpdateView):
    model = Service
    fields = ['name', 'type', 'start_time',
        'end_time', 'doctors', 'availability']
    template_name_suffix = '_update_form'


class ServiceDeleteView(DeleteView):
    model = Service
    success_url = '/clinics'

@login_required(login_url="/accounts/signin/")
def book(request):

    if (Aviews.is_receptionist(request.user)):

        if request.method == 'POST':
            form = forms.BookR(request.POST)
            if form.is_valid():
                x = form.save(commit=False)
                if str(x.Doctor.expertise) == str(x.Clinic):
                    
                    if request.POST["TOR"] > str(x.Clinic.start_time) and request.POST["TOR"] < str(x.Clinic.end_time):
                        if Reservation.rManager.filter(Day=request.POST['DOR'] , Clinic=request.POST['Clinic']).exists():
                            if Reservation.rManager.filter(Time=request.POST['TOR'] , Clinic=request.POST['Clinic']).exists():
                                form = forms.BookR()
                                message = 'please choose another time slot'
                                Title="Receptionist Booking"
                                return render(request, 'book/book.html', {'form': form, 'message': message, 'Title':Title})
                            else:
                                x.Time = request.POST["TOR"]
                                x.Day = request.POST["DOR"]
                                x.Booker = request.user
                                #x.Clinic.no_appointments += 1
                                x.save()
                                return render(request, 'clinics/service_list.html', {'success':"DONE!!",'Services':Service.objects.all(),'Title':"Services" })
                        else:
                            x.Time = request.POST["TOR"]
                            x.Day = request.POST["DOR"]
                            x.Booker = request.user
                            #x.Clinic.no_appointments += 1
                            x.save()
                            return render(request, 'clinics/service_list.html', {'success':"DONE!!",'Services':Service.objects.all(),'Title':"Services" })

                    else:
                            form = forms.BookR()
                            Title = "Receptionist Booking"
                            Dmessage = 'please choose between interval'
                            return render(request, 'book/book.html', {'form': form, 'Dmessage': Dmessage,'Title':Title})
                else:
                    form = forms.BookR()
                    Title = "Book"
                    Dmessage = 'please a doctor enrolled in this clinic'
                    return render(request, 'book/book.html', {'form': form, 'Dmessage': Dmessage, 'Title': Title})
        else:
            Title = "Receptionist Booking"
            form = forms.BookR()
            return render(request, 'book/book.html', {'form': form, 'Title':Title})


    else:

        if request.method == 'POST':
            form = forms.Book(request.POST)
            if form.is_valid():
                x = form.save(commit=False)
                if str(x.Doctor.expertise) == str(x.Clinic):
                    
                    if request.POST["TOR"] > str(x.Clinic.start_time) and request.POST["TOR"] < str(x.Clinic.end_time) :                           
                                
                        if Reservation.rManager.filter(Day=request.POST['DOR'], Clinic=request.POST['Clinic']).exists():
                            if Reservation.rManager.filter(Time=request.POST['TOR'], Clinic=request.POST['Clinic']).exists():
                                form = forms.Book()
                                Title = "Book"
                                message = 'please choose another time slot'
                                return render(request, 'book/book.html', {'form': form, 'message': message, 'Title': Title})
                            else:
                                

                                x.Booker = request.user
                                x.Time= request.POST["TOR"]
                                x.Day= request.POST["DOR"]
                                x.Patient = str(request.user.get_username())
                                #x.Clinic.no_appointments +=1
                                x.save()
                                return render(request, 'clinics/service_list.html', {'success':"DONE!!",'Services':Service.objects.all(),'Title':"Services" })
                        else:
                            
                            x.Booker = request.user
                            x.Time= request.POST["TOR"]
                            x.Day= request.POST["DOR"]
                            x.Patient = str(request.user.get_username())
                            #x.Clinic.no_appointments +=1
                            x.save()
                            request.session['success']= "DONE!"
                            return render(request, 'clinics/service_list.html', {'success':"DONE!!",'Services':Service.objects.all(),'Title':"Services" }) 
                    else:
                        form = forms.Book()
                        Title = "Book"
                        message = 'please choose between interval'
                        return render(request, 'book/book.html', {'form': form, 'message': message, 'Title': Title})
                
                else:
                    form = forms.Book()
                    Title = "Book"
                    Dmessage = 'please a doctor enrolled in this clinic'
                    return render(request, 'book/book.html', {'form': form, 'Dmessage': Dmessage, 'Title': Title})
                        
        else:
            Title = "Book"
            form = forms.Book()
            return render(request, 'book/book.html', {'form': form, 'Title': Title})
