from django.db import models
from django.utils.module_loading import import_string

def get_classroom_model():
    return import_string('apps.classes.models.Classroom')

def get_student_model():
    return import_string('apps.students.models.Student')


class Attendance(models.Model):
    student = models.ForeignKey('students.Student', on_delete=models.CASCADE, related_name='attendance_records')
    classroom = models.ForeignKey('classes.Classroom', on_delete=models.CASCADE, related_name='class_attendance')
    date = models.DateField()
    present = models.BooleanField(default=False)

    class Meta:
        unique_together = ('student', 'classroom', 'date')

    def __str__(self):
        status = "Present" if self.present else "Absent"
        return f"{self.student.full_name} - {self.date} ({status})"


# from django.db import models


# class Attendance(models.Model):
#     # classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
#     classroom = models.ForeignKey('classes.Classroom', on_delete=models.CASCADE)
#     # student = models.ForeignKey(Student, on_delete=models.CASCADE)
#     student = models.ForeignKey('students.Student', on_delete=models.CASCADE, related_name='attendance_records')
#     date = models.DateField()
#     present = models.BooleanField(default=False)

#     class Meta:
#         unique_together = ('classroom', 'student', 'date')

