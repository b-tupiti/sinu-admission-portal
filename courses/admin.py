from django.contrib import admin
from .models.course import Course
from .models.unit import Unit
from .models.courseunit import CourseUnit
from .models.studyperiod import StudyPeriod

class CourseAdmin(admin.ModelAdmin):
    pass
admin.site.register(Course, CourseAdmin)

class UnitAdmin(admin.ModelAdmin):
    list_display = ('code','title')
admin.site.register(Unit, UnitAdmin)

class CourseUnitAdmin(admin.ModelAdmin):
    pass
admin.site.register(CourseUnit, CourseUnitAdmin)

class StudyPeriodAdmin(admin.ModelAdmin):
    pass
admin.site.register(StudyPeriod, StudyPeriodAdmin)

