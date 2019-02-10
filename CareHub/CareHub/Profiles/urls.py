
from django.contrib import admin
from django.urls import path
from .import views

app_name = 'profile_page'
urlpatterns = [
    path(r'', views.profile, name="profile"),
    path(r'edit', views.profile_edit),


]
