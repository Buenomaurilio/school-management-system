from django.urls import path, include
from django.shortcuts import redirect
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('teacher/', include('teachers.urls')),
    path('student/', include('students.urls')),
    path('', lambda request: redirect('accounts/login/')),
]
