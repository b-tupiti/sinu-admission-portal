from django.db import models
from .courseunit import CourseUnit

class PrerequisiteGroup(models.Model):
    name = models.CharField(
        verbose_name='Prerequisite Group (name format - [Course Code]-[Unit Code]-[1])', 
        max_length=50,
    )
    course_unit = models.ForeignKey(
        CourseUnit, 
        on_delete=models.CASCADE,
        related_name='prerequisite_groups',
    )
    
    def __str__(self):
        return self.name