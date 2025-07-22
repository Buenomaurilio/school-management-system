from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib import messages
from apps.teachers.models import Teacher
from apps.students.models import Student

class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        user = self.request.user

        # Verifica se está associado a uma organização
        if not hasattr(user, 'organization') and not hasattr(user, 'teacher') and not hasattr(user, 'student'):
            messages.error(self.request, "No role or organization linked to your account.")
            return reverse_lazy('login')

        if hasattr(user, 'teacher'):
            return reverse_lazy('dashboard_teacher')

        elif hasattr(user, 'student'):
            return reverse_lazy('dashboard_student')

        elif user.is_superuser:
            return reverse_lazy('dashboard_admin')

        else:
            messages.error(self.request, "Invalid user role.")
            return reverse_lazy('login')

@login_required
def redirect_after_login(request):
    user = request.user

    if user.role == 'teacher':
        return redirect('teacher_dashboard')  # Nome da URL do dashboard do professor
    elif user.role == 'admin':
        return redirect('/admin/')  # ou um painel personalizado
    else:
        return redirect('student_dashboard')
