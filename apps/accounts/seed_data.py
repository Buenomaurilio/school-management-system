import os
import django
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(BASE_DIR)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'school_system.settings')
django.setup()

from django.contrib.auth import get_user_model
from apps.organizations.models import Organization
from apps.teachers.models import Teacher
from apps.students.models import Student
from apps.classes.models import Classroom, ClassGroup, Enrollment, Attendance

def run():
    User = get_user_model()

    # Criação da Organização
    org, _ = Organization.objects.get_or_create(name="English Academy")

    # Superusuário (admin)
    if not User.objects.filter(username="admin").exists():
        User.objects.create_superuser(username="admin", email="admin@example.com", password="admin123")

    # Professores
    for i in range(1, 3):
        user, _ = User.objects.get_or_create(username=f"teacher{i}", email=f"teacher{i}@school.com")
        user.set_password("123456")
        user.save()
        Teacher.objects.get_or_create(user=user, organization=org)

    # Alunos
    for i in range(1, 6):
        user, _ = User.objects.get_or_create(username=f"student{i}", email=f"student{i}@school.com")
        user.set_password("123456")
        user.save()
        Student.objects.get_or_create(user=user, organization=org)

    # Turma
    teacher = Teacher.objects.first()
    classroom, _ = ClassGroup.objects.get_or_create(
        name="Evening Class",
        organization=org,
        teacher=teacher,
        schedule="Mon/Wed/Fri 18:00–20:00"
    )

    # Matrícula dos alunos
    for student in Student.objects.all():
        Enrollment.objects.get_or_create(student=student, class_group=classroom)

    # Registrar presença para hoje
    from datetime import date
    for student in Student.objects.all():
        Attendance.objects.get_or_create(student=student, class_group=classroom, date=date.today(), present=True)

    print("✅ Dados de teste inseridos com sucesso.")
