from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            # Redirecionar com base no papel (role)
            if user.role == 'admin':
                return redirect('/admin/')
            elif user.role == 'teacher':
                return redirect('/teacher/dashboard/')
            elif user.role == 'student':
                return redirect('/student/dashboard/')
            elif user.role == 'secretary':
                return redirect('/secretary/')
            else:
                return redirect('/')  # fallback
    else:
        form = AuthenticationForm()

    return render(request, 'accounts/login.html', {'form': form})



@login_required
def redirect_after_login(request):
    user = request.user

    if user.role == 'teacher':
        return redirect('teacher_dashboard')  # Nome da URL do dashboard do professor
    elif user.role == 'admin':
        return redirect('/admin/')  # ou um painel personalizado
    else:
        return redirect('student_area')  # criaremos isso depois
