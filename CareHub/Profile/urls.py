
from django.conf.urls import url

from django.urls import path

from . import views

app_name = 'Profile'
urlpatterns = [
    url(r'^(?P<name>.+)/$$', views.patient, name='patient'),
    path('<int:pk>/patient_update/', views.patient_update, name='patient_update'),
    path('<int:pk>/patient_update_form/',
         views.patient_update_form, name='patient_update_form',),


]
