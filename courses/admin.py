from django.contrib import admin
from .models.course import Course
from .models.unit import Unit

class CourseAdmin(admin.ModelAdmin):
    pass
admin.site.register(Course, CourseAdmin)

class UnitAdmin(admin.ModelAdmin):
    list_display = ('code','title')
admin.site.register(Unit, UnitAdmin)

