from django.contrib import admin
from .models import Teacher

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'organization', 'user')
    list_filter = ('organization',)
    search_fields = ('full_name', 'email')
