from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('^$',views.homepage),
    path('^staff',views.staff),
    path('^about',views.about),
    path('^patient',include('patient.urls')),
    path('^doctor',include('doctor.urls')),
    path('^clinic',include('clinic.ur')),
]
