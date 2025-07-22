from .views import manage_classroom_students
from django.urls import path
from . import views

# urlpatterns = [
#     path('dashboard/', views.teacher_dashboard, name='dashboard_teacher'),
#     path('attendance/<int:classroom_id>/', views.mark_attendance, name='mark_attendance'),
# ]


urlpatterns = [
    path('dashboard/', views.teacher_dashboard, name='dashboard_teacher'),
    path('attendance/<int:classroom_id>/', views.mark_attendance, name='mark_attendance'),
    path('classroom/<int:classroom_id>/students/', manage_classroom_students, name='manage_classroom_students'),
]
