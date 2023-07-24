from django.contrib import admin
from .models.faculty import Faculty
from .models.school import School
from .models.department import Department


class FacultyAdmin(admin.ModelAdmin):
    pass
admin.site.register(Faculty, FacultyAdmin)

class SchoolAdmin(admin.ModelAdmin):
    list_display = ('name', 'abbr', 'faculty')
admin.site.register(School,SchoolAdmin)

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'abbr', 'school')
admin.site.register(Department, DepartmentAdmin)
