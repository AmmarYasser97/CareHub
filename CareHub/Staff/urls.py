from django.urls import path, include
from .views import DoctorListView, DoctorDetailView, DoctorUpdateView,\
    DoctorCreateView, DoctorDeleteView
from . import views

urlpatterns = [
    path('', DoctorListView.as_view(), name='staff-list'),
    path('<int:pk>/', DoctorDetailView.as_view(), name='staff-detail'),
    path('<int:pk>/update', DoctorUpdateView.as_view(), name='staff-update'),
    path('add/', DoctorCreateView.as_view(), name='staff-add'),
    path('<int:pk>/delete', DoctorDeleteView.as_view(), name='staff-delete'),

]
