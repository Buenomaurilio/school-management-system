from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from apps.classes.models import Classroom
from apps.teachers.models import Teacher

@login_required
def teacher_dashboard(request):
    try:
        teacher = request.user.teacher
        classrooms = Classroom.objects.filter(teacher=teacher)
    except Teacher.DoesNotExist:
        classrooms = []

    return render(request, 'teachers/dashboard.html', {
        'classrooms': classrooms
    })
