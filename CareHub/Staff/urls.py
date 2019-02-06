from django.urls import path, include
from .views import DoctorListView, DoctorDetailView
from . import views

urlpatterns = [
    path('', DoctorListView.as_view(), name='staff-home'),
    path('<int:pk>/', DoctorDetailView.as_view(), name='staff-detail'),
    # path('<int:pk>/edit', DoctorEditView.as_view(), name='staff-edit'),
    # path('add/', DoctorAddView.as_view(), name='staff-add'),

]
