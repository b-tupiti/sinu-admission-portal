from django.db import models
from .application import Application


class Employment(models.Model):
    
    application = models.ForeignKey(
        Application,
        related_name='application_employments',
        on_delete=models.CASCADE,
    )
    
    firm = models.CharField(
        max_length=255,
        verbose_name='Organization / Company',
        null=True,
        blank=True,
    )
    
    job_title = models.CharField(
        max_length=255,
        verbose_name='Job Title',
        null=True,
        blank=True,
    )
    
    month_year_started = models.DateField(
        verbose_name='Month/Year Started',
        null=True,
        blank=True,
    )
    
    month_year_ended = models.DateField(
        verbose_name='Month/Year Ended',
        null=True,
        blank=True,
    )
    
    is_current = models.BooleanField(
        verbose_name='Current Employment',
        null=True,
        blank=True,
    )
    
    def __str__(self):
        return str(self.firm)