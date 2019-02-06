from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^accounts/', include('accounts.urls')),
    path('staff/', include('Staff.urls')),
    path('clinics/', include('Clinics.urls')),
    path('scans/', include('Scans.urls')),
]

urlpatterns += staticfiles_urlpatterns()
