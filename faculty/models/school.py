from django.db import models
from .faculty import Faculty

class School(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name of School')
    abbr = models.CharField(max_length=100, verbose_name='School Abbreviation', null=True, blank=True)
    faculty = models.ForeignKey(Faculty, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        if self.abbr:
            return ' - '.join([self.name, self.abbr])
        return self.name