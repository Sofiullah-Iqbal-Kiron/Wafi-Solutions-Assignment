from django.contrib import admin
from .models import Employee


class EmployeeAdmin(admin.ModelAdmin):
    list_display = [
        "full_name",
        "mobile",
        "department",
        "designation",
        "still_employee"
    ]
    list_editable = [
        "department",
        "designation"
    ]
    fieldsets = [
        ("Personal Information", {"fields": [("first_name", "last_name"), ("email", "mobile"), "date_of_birth", "photo"]}),
        ("Employment Related Fields", {"fields": ["date_of_joining", ("department", "designation"), "salary", "date_of_leave"]}),
        ("Verbose and Optionals", {"classes": ["collapse"], "fields": ["responsibilities"]})
    ]


admin.site.register(Employee, EmployeeAdmin)
