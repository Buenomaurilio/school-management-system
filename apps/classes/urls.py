from django.urls import path
from .views import enrollment_create_view

urlpatterns = [
    path('enroll/', enrollment_create_view, name='enrollment_create'),
]
