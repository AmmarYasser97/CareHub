from django.conf.urls import url
from . import views

app_name = 'accounts'

urlpatterns = [
   url(r'^signup/$', views.SignUp, name = 'signup'),
   url(r'^$', views.profile, name = 'profile'),
   url(r'^signin/$', views.SignIn, name = 'signin'),
   url(r'^signout/$', views.SignOut, name = 'signout'),
   url(r'^Receptionist/$', views.Receptionist, name = 'receptionist'),
]
