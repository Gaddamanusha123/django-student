from django.contrib import admin
from .models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'course')
    
admin.site.register(Student, StudentAdmin)