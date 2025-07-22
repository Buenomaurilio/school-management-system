from apps.organizations.models import Organization
from apps.teachers.models import Teacher
from apps.students.models import Student
from django.db import models


class Classroom(models.Model):
    name = models.CharField(max_length=100)
    organization = models.ForeignKey('organizations.Organization', on_delete=models.CASCADE)
    teacher = models.ForeignKey('teachers.Teacher', on_delete=models.CASCADE, related_name='classrooms')
    students = models.ManyToManyField('students.Student', blank=True, related_name='classrooms', db_table='classes_classroom_students')

    schedule = models.CharField(max_length=100)
    room = models.CharField(max_length=50, blank=True)
    level = models.CharField(max_length=50)

    class Meta:
        app_label = 'classes'

    def __str__(self):
        return f"{self.name} ({self.organization.name})"


class ClassGroup(models.Model):
    name = models.CharField(max_length=100)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)
    schedule = models.CharField(max_length=100)  # Ex: "Mon/Wed/Fri 9:00–11:00"
    
    class Meta:
        app_label = 'classes'

    def __str__(self):
        return f"{self.name} ({self.schedule})"



class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    class_group = models.ForeignKey(ClassGroup, on_delete=models.CASCADE)
    date_enrolled = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ('student', 'class_group')

    def __str__(self):
        return f"{self.student} - {self.class_group}"


class Attendance(models.Model):
    student = models.ForeignKey('students.Student', on_delete=models.CASCADE, related_name='class_attendance')
    class_group = models.ForeignKey(ClassGroup, on_delete=models.CASCADE)
    date = models.DateField()
    present = models.BooleanField(default=True)

    class Meta:
        unique_together = ('student', 'class_group', 'date')

    def __str__(self):
        status = "Present" if self.present else "Absent"
        return f"{self.student} - {status} on {self.date}"
