from django.urls import path, include
from django.conf.urls import url
from .views import ServiceListView, ServiceDetailView, ServiceUpdateView,\
    ServiceCreateView, ServiceDeleteView, ClinicListView, ScanListView

from . import views


urlpatterns = [
    path('', ServiceListView.as_view(), name='service-list'),
    path('clinics/', ClinicListView.as_view(), name='clinic-list'),
    path('scans/', ScanListView.as_view(), name='scan-list'),
    path('<int:pk>/', ServiceDetailView.as_view(), name='service-detail'),
    path('<int:pk>/update', ServiceUpdateView.as_view(), name='service-update'),
    path('add/', ServiceCreateView.as_view(), name='service-add'),
    path('<int:pk>/delete', ServiceDeleteView.as_view(), name='service-delete'),

]
