from django.db import models
from django.urls import reverse

class Unit(models.Model):
    code = models.CharField(max_length=20,verbose_name='Unit Code', unique=True)
    title = models.CharField(max_length=255)
    
    def __str__(self):
        return self.title