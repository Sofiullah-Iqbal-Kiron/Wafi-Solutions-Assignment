from django.contrib import admin

from company.models import Department, Designation


class DesignationAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'department'
    ]
    radio_fields = {
        'department': admin.VERTICAL
    }


admin.site.register(Department)
admin.site.register(Designation, DesignationAdmin)
