from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Subject)
admin.site.register(Class)

class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'roll', 'is_active']
admin.site.register(Student, StudentAdmin)