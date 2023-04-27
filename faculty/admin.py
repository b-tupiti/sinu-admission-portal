from django.contrib import admin
from .models import Faculty, School, Department

class FacultyAdmin(admin.ModelAdmin):
    pass
admin.site.register(Faculty, FacultyAdmin)

class SchoolAdmin(admin.ModelAdmin):
    pass
admin.site.register(School,SchoolAdmin)

class DepartmentAdmin(admin.ModelAdmin):
    pass
admin.site.register(Department, DepartmentAdmin)
