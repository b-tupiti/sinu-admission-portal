from django.apps import AppConfig


class CoursesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'courses'
    
    def ready(self):
        from .models.course import Course
        from .models.unit import Unit
        from .models.courseunit import CourseUnit
        from .models.studyperiod import StudyPeriod
        from .models.prerequisite import Prerequisite
        from .models.prerequisite_group import PrerequisiteGroup
