from django.contrib import admin
from .models import Course, Unit

class CourseAdmin(admin.ModelAdmin):
    pass
admin.site.register(Course, CourseAdmin)

class UnitAdmin(admin.ModelAdmin):
    list_display = ('code','title')
admin.site.register(Unit, UnitAdmin)

