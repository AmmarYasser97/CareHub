from django.urls import path, include
from django.conf.urls import url

from . import views

app_name='services'

urlpatterns = [
    url(r'^$', views.clinicslist,name='cl'),

    url(r'^createService/$', views.create, name="create"),
    
]
