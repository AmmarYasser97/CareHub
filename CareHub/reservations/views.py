from django.shortcuts import render,redirect
from . import forms
# Create your views here.
def book(request):
    if request.method=='POST':
        form=forms.Book(request.POST)
        if form.is_valid():
            x=form.save(commit=False)
            x.Patient=request.user
            x.save()
            return redirect('services:cl')

    else:
        form = forms.Book()
    return render(request,'book/book.html',{'form':form})
