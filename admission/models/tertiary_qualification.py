from django.db import models
from .application import Application


class TertiaryQualification(models.Model):
    application = models.ForeignKey(
        Application,
        related_name='institutions',
        on_delete=models.CASCADE,
    )
    
    name = models.CharField(
        max_length=255,
        verbose_name='Instition',
        null=True,
        blank=True,
    )
    
    course = models.CharField(
        max_length=255,
        verbose_name='Course / Qualification',
        null=True,
        blank=True,
    )
    
    year_start = models.IntegerField(
        verbose_name='Year Started',
        null=True,
        blank=True,
    )
    
    year_end = models.IntegerField(
        verbose_name='Year Ended',
        null=True,
        blank=True,
    )
    
    major = models.CharField(
        max_length=255,
        verbose_name='Major Field of Study',
        null=True,
        blank=True,
    )