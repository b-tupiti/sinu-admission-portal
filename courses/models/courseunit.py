from django.urls import reverse
from django.db import models
from .course import Course
from .unit import Unit
from .studyperiod import StudyPeriod

class CourseUnit(models.Model):
    
    class Meta:
        unique_together = ('unit', 'course')
        
    unit = models.ForeignKey(Unit, verbose_name='Select Unit', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, verbose_name='Select Course', on_delete=models.CASCADE)
    unit_type = models.CharField(
        verbose_name='Unit Type',
        choices=(('core', 'Core'), ('elective', 'Elective')), 
        max_length=10,
        blank=True,
        null=True,
    )
    credit_points = models.IntegerField(
        verbose_name='Credit Points',
        null=True,
        blank=True,
    )
    study_period = models.ManyToManyField(
        StudyPeriod, 
        blank=True,
    )
    offer_year = models.CharField(
        verbose_name='Offer Year',
        choices=(
            ('year_1', 'Year 1'), 
            ('year_2', 'Year 2'),
            ('year_3', 'Year 3'),
            ('year_4', 'Year 4'),
        ), 
        max_length=10,
        blank=True,
        null=True,
    )

        
    def __str__(self):
        return self.unit.title
    
    