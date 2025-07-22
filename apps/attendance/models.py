from django.db import models
from apps.classes.models import Classroom
from apps.students.models import Student

class Attendance(models.Model):
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    # student = models.ForeignKey(Student, on_delete=models.CASCADE)
    student = models.ForeignKey('students.Student', on_delete=models.CASCADE, related_name='attendance_records')
    date = models.DateField()
    present = models.BooleanField(default=False)

    class Meta:
        unique_together = ('classroom', 'student', 'date')

    def __str__(self):
        status = "Present" if self.present else "Absent"
        return f"{self.student.full_name} - {self.date} ({status})"
