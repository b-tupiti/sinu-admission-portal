from django.db import models
from django.urls import reverse

class Course(models.Model):
    """
    Represents the singlemost Course/Program offered by a School.
    """
    class QLevel(models.TextChoices):
        DEGREE = "degree", "degree",
        PRE_DEGREE = "pre-degree","pre-degree"
        CERTIFICATE = "certificate", "certificate"
        ADVANCED_CERTIFICATE = "advanced certificate", "advanced certificate"
        DIPLOMA = "diploma", "diploma"
        PRE_DIPLOMA = "pre-diploma", "pre-diploma"
        POSTGRADUATE_DIPLOMA = "postgraduate diploma", "postgraduate diploma"
        MASTER_DEGREE = "master degree", "master degree"
    
    class Campus(models.TextChoices):
        KUKUM = "kukum", "kukum",
        MARINE = "marine", "marine",
        PANATINA = "panatina", "panatina",
        
    class DurationType(models.TextChoices):
        YEAR = "year", "year"
        MONTH = "month", "month"
        WEEK = "week", "week"
        
    code = models.CharField(
        max_length=20, 
        verbose_name='Course Code',
        unique=True,
        )
    title = models.CharField(
        max_length=200,
        verbose_name='Course Title',
    ) 
    qualification_level = models.CharField(
        max_length=50,
        choices=QLevel.choices,
        null=True,
        blank=True,
    )
    description = models.TextField(
        verbose_name='Course Description',
        null=True,
        blank=True,
    )
 
    campus = models.CharField(
        verbose_name='Campus',
        max_length=10,
        choices=Campus.choices,
        null=True,
        blank=True,
    )  
  
    duration_type = models.CharField(
        verbose_name='Duration Type',
        max_length=5, 
        choices=DurationType.choices,
        null=True,
        blank=True,
    )
    
    duration_length = models.FloatField(
        verbose_name='Duration',
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("course-detail", kwargs={"code": self.code})
    

class Unit(models.Model):
    code = models.CharField(max_length=20,verbose_name='Unit Code', unique=True)
    title = models.CharField(max_length=255)
    
    def __str__(self):
        return self.title
