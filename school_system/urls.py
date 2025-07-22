from django.contrib.auth.views import LogoutView
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from django.http import HttpResponse

urlpatterns = [
    path('admin/', admin.site.urls),

    # Apps
    path('accounts/', include('apps.accounts.urls')),
    path('teacher/', include('apps.teachers.urls')),
    path('student/', include('apps.students.urls')),

    path('logout/', LogoutView.as_view(), name='logout'),
    path('admins/', include('apps.admins.urls')),
    path('classes/', include('apps.classes.urls')),

    path('', lambda request: redirect('login')),
]
