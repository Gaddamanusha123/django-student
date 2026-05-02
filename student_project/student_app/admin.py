from django.contrib import admin
from django import forms
from simple_history.admin import SimpleHistoryAdmin
from .models import Student, HistoricalStudent


#  CUSTOM FORM

class StudentAdminForm(forms.ModelForm):
    change_reason = forms.CharField(
        required=False,
        label="Change Reason",
        widget=forms.Textarea(attrs={"rows": 2})
    )

    class Meta:
        model = Student
        fields = "__all__"


#  STUDENT ADMIN
@admin.register(Student)
class StudentAdmin(SimpleHistoryAdmin):
    form = StudentAdminForm

    def get_list_display(self, request):
        if request.user.is_superuser:
            return (
                'id', 'name', 'age', 'course',
                'roll_number', 'status',
                'is_active', 'joined_date'
            )
        return ('id', 'name', 'course', 'status')

    def get_fields(self, request, obj=None):
        if request.user.is_superuser:
            return (
                'name', 'age', 'course', 'roll_number',
                'status', 'joined_date',
                'is_active', 'profile_url',
                'extra_data',
                'change_reason'
            )
        return ('name', 'course', 'status')

    def get_readonly_fields(self, request, obj=None):
        return ('joined_date',)



    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_add_permission(self, request):
        return request.user.is_superuser

    def has_change_permission(self, request, obj=None):
        return True
    def has_view_history_permission(self, request, obj=None):
        return True   # allow button for all

    def save_model(self, request, obj, form, change):
        if not obj.age:
            obj.age = 0
        if not obj.roll_number:
            obj.roll_number = "N/A"

        reason = form.cleaned_data.get("change_reason")
        if reason:
            obj._change_reason = reason

        super().save_model(request, obj, form, change)

    search_fields = ('name', 'roll_number', 'course')
    list_filter = ('status', 'is_active', 'joined_date')
    ordering = ('-id',)


#  GLOBAL HISTORY (ADMIN ONLY)
@admin.register(HistoricalStudent)
class StudentHistoryAdmin(admin.ModelAdmin):

    def has_module_permission(self, request):
        return request.user.is_superuser

    def has_view_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    # Global history view
    list_display = (
        'id',
        'name',
        'roll_number',
        'status',
        'history_user',          
        'history_date',
        'history_type',
        'history_change_reason'  
    )

    list_filter = ('history_type', 'status', 'history_date')
    search_fields = ('name', 'roll_number')
    ordering = ('-history_date',)