from django.db import models

class StudyPeriod(models.Model):
    study_period = models.CharField(
        verbose_name='Study Period',
        max_length=20,
    )
    
    