from django.db import models
from apps.organizations.models import Organization
from accounts.models import User

class Student(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True, limit_choices_to={'role': 'student'})
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    date_of_birth = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
