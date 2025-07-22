from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from apps.attendance.models import Attendance
from django.shortcuts import render, redirect
from apps.classes.models import Classroom
from apps.students.models import Student
from apps.teachers.models import Teacher
from django.utils.timezone import now
from django.contrib import messages

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


@login_required
@csrf_protect
def mark_attendance(request, classroom_id):
    teacher = request.user.teacher
    classroom = Classroom.objects.get(id=classroom_id, teacher=teacher)
    students = Student.objects.filter(classrooms=classroom)

    if request.method == 'POST':
        date = request.POST.get('date') or now().date()
        present_ids = request.POST.getlist('present')

        for student in students:
            Attendance.objects.update_or_create(
                student=student,
                classroom=classroom,
                date=date,
                defaults={'present': str(student.id) in present_ids}
            )

        messages.success(request, "Attendance saved successfully.")
        # return redirect_stderr('dashboard_teacher')
        return redirect('dashboard_teacher')

    return render(request, 'teachers/mark_attendance.html', {
        'classroom': classroom,
        'students': students
    })



@login_required
@require_http_methods(["GET", "POST"])
def manage_classroom_students(request, classroom_id):
    teacher = request.user.teacher
    classroom = Classroom.objects.get(id=classroom_id, teacher=teacher)

    # alunos da mesma organização do professor
    all_students = Student.objects.filter(organization=teacher.organization)

    if request.method == 'POST':
        selected_ids = request.POST.getlist('students')
        selected_students = Student.objects.filter(id__in=selected_ids)
        classroom.students.set(selected_students)
        classroom.save()
        messages.success(request, "Classroom students updated successfully.")
        return redirect('dashboard_teacher')

    current_students = classroom.students.all()

    return render(request, 'teachers/manage_classroom_students.html', {
        'classroom': classroom,
        'all_students': all_students,
        'current_students': current_students,
    })
