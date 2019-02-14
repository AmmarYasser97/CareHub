from django.shortcuts import render

def home (request):
    Title= 'Welcome'
    return render(request, 'index.html',{'Title':Title})
