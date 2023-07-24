from django.db import models


class Faculty(models.Model):
    
    class Meta:
        verbose_name_plural = 'Faculties'
        
    name = models.CharField(max_length=100, verbose_name='Name of Faculty')
    abbr = models.CharField(max_length=10, verbose_name='Faculty Abbreviation')
    
    def __str__(self):
        return ' - '.join([self.name, self.abbr])