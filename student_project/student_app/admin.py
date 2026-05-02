# from django.contrib import admin
# from django import forms
# from simple_history.admin import SimpleHistoryAdmin
# from .models import Student, HistoricalStudent


# # =========================
# # 🔹 CUSTOM FORM (IMPORTANT)
# # =========================
# class StudentAdminForm(forms.ModelForm):
#     change_reason = forms.CharField(
#         required=False,
#         label="Change Reason",
#         widget=forms.Textarea(attrs={"rows": 2})
#     )

#     class Meta:
#         model = Student
#         fields = "__all__"


# # =========================
# # 🔹 STUDENT ADMIN
# # =========================
# @admin.register(Student)
# class StudentAdmin(SimpleHistoryAdmin):
#     form = StudentAdminForm   # ✅ attach custom form

#     # ✅ List display
#     def get_list_display(self, request):
#         if request.user.is_superuser:
#             return (
#                 'id', 'name', 'age', 'course',
#                 'roll_number', 'status',
#                 'is_active', 'joined_date'
#             )
#         return ('id', 'name', 'course', 'status')

#     # ✅ Fields in form
#     def get_fields(self, request, obj=None):
#         if request.user.is_superuser:
#             return (
#                 'name', 'age', 'course', 'roll_number',
#                 'status', 'joined_date',
#                 'is_active', 'profile_url',
#                 'extra_data',
#                 'change_reason'   # 🔥 SHOW FIELD HERE
#             )
#         return ('name', 'course', 'status')

#     # ✅ Read-only
#     def get_readonly_fields(self, request, obj=None):
#         return ('joined_date',)

#     # 🔒 Permissions
#     def has_delete_permission(self, request, obj=None):
#         return request.user.is_superuser

#     def has_view_history_permission(self, request, obj=None):
#         return request.user.is_superuser

#     def has_add_permission(self, request):
#         return request.user.is_superuser

#     def has_change_permission(self, request, obj=None):
#         return True

#     # 🔥 SAVE CHANGE REASON CORRECTLY
#     def save_model(self, request, obj, form, change):
#         if not obj.age:
#             obj.age = 0
#         if not obj.roll_number:
#             obj.roll_number = "N/A"

#         # ✅ Get reason from form
#         reason = form.cleaned_data.get("change_reason")

#         if reason:
#             obj._change_reason = reason   # 🔥 THIS IS KEY

#         super().save_model(request, obj, form, change)

#     # ✅ Search
#     search_fields = ('name', 'roll_number', 'course')

#     # ✅ Filters
#     list_filter = ('status', 'is_active', 'joined_date')

#     # ✅ Ordering
#     ordering = ('-id',)


# # =========================
# # 🔥 GLOBAL HISTORY ADMIN
# # =========================
# @admin.register(HistoricalStudent)
# class StudentHistoryAdmin(admin.ModelAdmin):

#     def has_module_permission(self, request):
#         return request.user.is_superuser

#     def has_view_permission(self, request, obj=None):
#         return request.user.is_superuser

#     def has_add_permission(self, request):
#         return False

#     def has_change_permission(self, request, obj=None):
#         return False

#     def has_delete_permission(self, request, obj=None):
#         return False

#     list_display = (
#         'id',
#         'name',
#         'roll_number',
#         'status',
#         'history_user',
#         'history_date',
#         'history_type',
#         'history_change_reason'
#     )

#     list_filter = ('history_type', 'status', 'history_date')
#     search_fields = ('name', 'roll_number')
#     ordering = ('-history_date',)


# def history_view(self, request, object_id, extra_context=None):
#     extra_context = extra_context or {}

#     if not request.user.is_superuser:
#         extra_context["limited_history"] = True

#     return super().history_view(request, object_id, extra_context=extra_context)



from django.contrib import admin
from django import forms
from simple_history.admin import SimpleHistoryAdmin
from .models import Student, HistoricalStudent


# =========================
# 🔹 CUSTOM FORM
# =========================
class StudentAdminForm(forms.ModelForm):
    change_reason = forms.CharField(
        required=False,
        label="Change Reason",
        widget=forms.Textarea(attrs={"rows": 2})
    )

    class Meta:
        model = Student
        fields = "__all__"


# =========================
# 🔹 STUDENT ADMIN
# =========================
@admin.register(Student)
class StudentAdmin(SimpleHistoryAdmin):
    form = StudentAdminForm

    # ✅ List display
    def get_list_display(self, request):
        if request.user.is_superuser:
            return (
                'id', 'name', 'age', 'course',
                'roll_number', 'status',
                'is_active', 'joined_date'
            )
        return ('id', 'name', 'course', 'status')

    # ✅ Fields
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

    # ✅ Read-only
    def get_readonly_fields(self, request, obj=None):
        return ('joined_date',)

    # 🔒 Permissions

    # ❌ Only admin can delete
    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser

    # ❌ Only admin can add
    def has_add_permission(self, request):
        return request.user.is_superuser

    # ✅ Everyone can edit
    def has_change_permission(self, request, obj=None):
        return True

    # 🔥 LIMITED HISTORY ACCESS

    # 👉 Admin → full history
    # 👉 Normal user → only object-level history
    def has_view_history_permission(self, request, obj=None):
        return True   # allow button for all

    # 🔥 Save change reason
    def save_model(self, request, obj, form, change):
        if not obj.age:
            obj.age = 0
        if not obj.roll_number:
            obj.roll_number = "N/A"

        reason = form.cleaned_data.get("change_reason")
        if reason:
            obj._change_reason = reason

        super().save_model(request, obj, form, change)

    # ✅ Search & filters
    search_fields = ('name', 'roll_number', 'course')
    list_filter = ('status', 'is_active', 'joined_date')
    ordering = ('-id',)


# =========================
# 🔥 GLOBAL HISTORY (ADMIN ONLY)
# =========================
@admin.register(HistoricalStudent)
class StudentHistoryAdmin(admin.ModelAdmin):

    # ❌ Hide from normal users
    def has_module_permission(self, request):
        return request.user.is_superuser

    def has_view_permission(self, request, obj=None):
        return request.user.is_superuser

    # ❌ No edit/delete
    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    # ✅ Global history view
    list_display = (
        'id',
        'name',
        'roll_number',
        'status',
        'history_user',          # changed by
        'history_date',
        'history_type',
        'history_change_reason'  # reason
    )

    list_filter = ('history_type', 'status', 'history_date')
    search_fields = ('name', 'roll_number')
    ordering = ('-history_date',)