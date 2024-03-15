from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('owner/login/', views.owner_login, name='owner_login'),
    path('staff/login/', views.staff_login, name='staff_login'),
    path('owner/dashboard/', views.owner_dashboard, name='owner_dashboard'),
    path('staff/dashboard/', views.staff_dashboard, name='staff_dashboard'),
    path('owner/profile/', views.owner_profile, name='owner_profile'),
    path('staff/profile/', views.staff_profile, name='staff_profile'),
    path('register/owner/', views.owner_register, name='owner_register'),
    path('register/staff/', views.staff_register, name='staff_register'),

]