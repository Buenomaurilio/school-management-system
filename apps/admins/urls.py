from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.admin_dashboard, name='dashboard_admin'),
]
