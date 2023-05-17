from django.contrib import admin
from django import forms
from django.db import models
from .models.course import Course
from .models.unit import Unit
from .models.courseunit import CourseUnit
from .models.studyperiod import StudyPeriod
from .models.prerequisite import Prerequisite
from .models.prerequisite_group import PrerequisiteGroup

    
class CourseUnitAdmin(admin.ModelAdmin):
     def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "unit":
            kwargs["queryset"] = Unit.objects.order_by("title")
        if db_field.name == "course":
            kwargs["queryset"] = Course.objects.order_by("title")
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
    
admin.site.register(CourseUnit, CourseUnitAdmin)


class PrerequisiteAdmin(admin.ModelAdmin):
    pass
admin.site.register(Prerequisite, PrerequisiteAdmin)

class PrerequisiteGroupAdmin(admin.ModelAdmin):
    pass
admin.site.register(PrerequisiteGroup, PrerequisiteGroupAdmin)


class CourseAdmin(admin.ModelAdmin):
    pass
admin.site.register(Course, CourseAdmin)

class UnitAdmin(admin.ModelAdmin):
    list_display = ('code','title')
admin.site.register(Unit, UnitAdmin)




class StudyPeriodAdmin(admin.ModelAdmin):
    pass
admin.site.register(StudyPeriod, StudyPeriodAdmin)

