from django.db import models
from .school import School


class Department(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name of Department')
    abbr = models.CharField(max_length=10, blank=True, null=True, verbose_name='Department Abbreviation')
    school = models.ForeignKey(School, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        if self.abbr:
            return ' - '.join([self.name, self.abbr])
        return self.name
    