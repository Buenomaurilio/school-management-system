from django.http import HttpResponseForbidden
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from classes.models import Classroom
from teachers.models import Teacher

@login_required
def teacher_dashboard(request):
    if not request.user.role == 'teacher':
        return HttpResponseForbidden("403 - Access Denied")
    # if not request.user.role == 'teacher':
    #     return render(request, '403.html')  # criar se quiser

    try:
        teacher = Teacher.objects.get(user=request.user)
    except Teacher.DoesNotExist:
        teacher = None

    classrooms = Classroom.objects.filter(teacher=teacher)

    return render(request, 'teachers/dashboard.html', {'classrooms': classrooms})
