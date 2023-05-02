from django.db import models
from .prerequisite_group import PrerequisiteGroup
from .courseunit import CourseUnit

class Prerequisite(models.Model):
    prerequisite_group = models.ForeignKey(
        PrerequisiteGroup,
        on_delete=models.CASCADE,
        related_name='prerequisites',
    )
    prerequisite = models.ForeignKey(
        CourseUnit,
        verbose_name='Prerequisite',
        on_delete=models.CASCADE,
    )
    
    def __str__(self):
        return self.prerequisite.unit.title