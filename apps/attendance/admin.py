from django.contrib import admin
from .models import Attendance

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('student', 'classroom', 'date', 'present')
    list_filter = ('date', 'classroom', 'present')
    search_fields = ('student__full_name',)
