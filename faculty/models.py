from django.db import models


class Faculty(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name of Faculty')
    abbr = models.CharField(max_length=10, verbose_name='Faculty Abbreviation')
    
    def __str__(self):
        return ' - '.join([self.name, self.abbr])
    
    
class School(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name of School')
    abbr = models.CharField(max_length=100, verbose_name='School Abbreviation', null=True, blank=True)
    faculty = models.ForeignKey(Faculty, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        if self.abbr:
            return ' - '.join([self.name, self.abbr])
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name of Department')
    abbr = models.CharField(max_length=10, blank=True, null=True, verbose_name='Department Abbreviation')
    school = models.ForeignKey(School, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return ' - '.join([self.name, self.abbr])
    

