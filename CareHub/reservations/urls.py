from django.urls import path, include
from django.conf.urls import url
from . import views

app_name='reservations'

urlpatterns=[
    url(r'^$',views.book,name='create'),
]