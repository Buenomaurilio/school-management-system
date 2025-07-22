# apps/accounts/management/commands/seed.py

from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from apps.organizations.models import Organization
from apps.teachers.models import Teacher
from apps.students.models import Student
from apps.classes.models import ClassGroup, Enrollment, Attendance
from datetime import date

class Command(BaseCommand):
    help = 'Seed database with initial data'

    def handle(self, *args, **kwargs):
        User = get_user_model()

        org, _ = Organization.objects.get_or_create(name="English Academy")

        # Superuser
        if not User.objects.filter(username="admin").exists():
            User.objects.create_superuser(username="admin", email="admin@example.com", password="admin123")

        # Teachers
        for i in range(1, 3):
            user, _ = User.objects.get_or_create(username=f"teacher{i}", email=f"teacher{i}@school.com")
            user.set_password("123456")
            user.save()
            Teacher.objects.get_or_create(user=user, organization=org)

        # Students
        for i in range(1, 6):
            user, _ = User.objects.get_or_create(username=f"student{i}", email=f"student{i}@school.com")
            user.set_password("123456")
            user.save()
            Student.objects.get_or_create(user=user, organization=org)

        teacher = Teacher.objects.first()
        class_group, _ = ClassGroup.objects.get_or_create(
            name="Evening Class",
            organization=org,
            teacher=teacher,
            schedule="Mon/Wed/Fri 18:00–20:00"
        )

        for student in Student.objects.all():
            Enrollment.objects.get_or_create(student=student, class_group=class_group)
            Attendance.objects.get_or_create(student=student, class_group=class_group, date=date.today(), present=True)

        self.stdout.write(self.style.SUCCESS("✅ Dados de teste inseridos com sucesso."))
