from django.db import models
from organizations.models import Organization
from accounts.models import User

class Teacher(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True, limit_choices_to={'role': 'teacher'})
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    hired_at = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.full_name
