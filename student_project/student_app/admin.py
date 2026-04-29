from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        if request.user.is_superuser:
            return ('id', 'name', 'age', 'course', 'roll_number')
        return ('id', 'name', 'course')

    def get_fields(self, request, obj=None):
        if request.user.is_superuser:
            return ('name', 'age', 'course', 'roll_number')
        return ('name', 'course')   


    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return ()
        return ()   

    
    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser


    def has_add_permission(self, request):
        return True


    def has_change_permission(self, request, obj=None):
        return True

    
    def save_model(self, request, obj, form, change):
        if not obj.age:
            obj.age = 0   # default value
        if not obj.roll_number:
            obj.roll_number = "N/A"
        super().save_model(request, obj, form, change)