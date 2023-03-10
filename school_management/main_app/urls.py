from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('students/', views.students, name='students'),
    path('add_studednt/', views.add_student, name='add-student'),
    path('edit_studednt/<int:id>', views.edit_student, name='edit-student'),
    path('delete_studednt/<int:id>', views.delete_student, name='delete-student'),

    path('class_subject/', views.class_subject, name='class-subject'),
    path('subject_marks_input/', views.subject_marks_input, name='subject-marks-input'),
]