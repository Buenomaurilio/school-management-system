from django.db import models
from organizations.models import Organization
from teachers.models import Teacher
from students.models import Student

class Classroom(models.Model):
    name = models.CharField(max_length=100)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, blank=True)
    students = models.ManyToManyField(Student, blank=True)
    schedule = models.CharField(max_length=100, help_text="e.g. Mon & Wed, 9:00 - 11:00 AM")
    room = models.CharField(max_length=50, blank=True)
    level = models.CharField(max_length=50, help_text="e.g. A1, B2, Advanced")

    def __str__(self):
        return f"{self.name} ({self.organization.name})"
