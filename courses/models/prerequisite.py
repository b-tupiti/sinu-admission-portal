from django.db import models
from .prerequisite_group import PrerequisiteGroup
from .courseunit import CourseUnit
from django.core.exceptions import ValidationError

class Prerequisite(models.Model):
    
    class Meta:
        unique_together = ('prerequisite_group','prerequisite')
        
    
    prerequisite_group = models.ForeignKey(
        PrerequisiteGroup,
        on_delete=models.CASCADE,
        related_name='grouped_prerequisites',
    )
    prerequisite = models.ForeignKey(
        CourseUnit,
        verbose_name='Prerequisite',
        on_delete=models.CASCADE,
        related_name='prerequisites',
    )
    
    def __str__(self):
        return self.prerequisite.unit.title
    
    def clean(self):
        course_unit = self.prerequisite_group.course_unit
        if course_unit == self.prerequisite:
            raise ValidationError(f'cannot set {self.prerequisite} as prerequisite of its own')
        
        # before adding a prereq, check if that prereq already exists in any prereq group of a unit
        # if it does, raise a validation error stating that 'unit is already a prerequisite in prereq group'
        
        # get the course_unit from the prereq group
        course_unit = self.prerequisite_group.course_unit
        
        # get all other prereq groups of the course unit
        prereq_groups = course_unit.prerequisite_groups.all()
        
        # check if this prerequisite exists in any of the group
        for group in prereq_groups:
            
            prerequisites = group.grouped_prerequisites
            #print(prerequisites.all())
            for prerequisite in prerequisites.all():
                # if it does, raise validation error
   
                if prerequisite.prerequisite.unit.code == self.prerequisite.unit.code:
                    raise ValidationError(f"{self.prerequisite} is already a prerequisite for this unit")
        
        