from django.contrib import admin
from .models import Classroom

@admin.register(Classroom)
class ClassroomAdmin(admin.ModelAdmin):
    list_display = ('name', 'organization', 'teacher', 'level', 'room')
    list_filter = ('organization', 'level')
    search_fields = ('name', 'room')
    filter_horizontal = ('students',)
