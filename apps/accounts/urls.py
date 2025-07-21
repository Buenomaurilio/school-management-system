from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import LoginView
from .views import redirect_after_login
from .views import login_view
from django.urls import path


urlpatterns = [
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('redirect/', redirect_after_login, name='redirect_after_login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]

