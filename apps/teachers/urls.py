from django.urls import path
from . import views


urlpatterns = [
    path('dashboard/', views.teacher_dashboard, name='dashboard_teacher'),
]
