from django.contrib import admin
from .models import *
# Register your models here.
#


admin.site.register(School)
admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(Class)































# admin.site.register(Subject)
# admin.site.register(Class)
#
# class StudentAdmin(admin.ModelAdmin):
#     list_display = ['name', 'roll','is_active']
#
#     # def get_class_name(self, obj):
#     #     return obj.class_name.name
#     # get_class_name.short_description = 'Author'
#
# admin.site.register(Student, StudentAdmin)