from django import forms
from apps.students.models import Student
from apps.classes.models import Enrollment, ClassGroup

class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = ['student', 'class_group']
