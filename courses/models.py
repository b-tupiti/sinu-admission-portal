from django.db import models
from django.urls import reverse

class Course(models.Model):
    """
    Represents the singlemost Course/Program offered by a School.
    """
    class QLevel(models.TextChoices):
        DEGR = "Degree", "Degree",
        CERT = "Certificate", "Certificate"
        DIPL = "Diploma", "Diploma"
        POSD = "Postgraduate Diploma", "Postgraduate Diploma"
        MAST = "Masters", "Masters"
    
    class Campus(models.TextChoices):
        KUK = "Kukum", "Kukum",
        MAR = "Marine", "Marine",
        PAN = "Panatina", "Panatina",
        
    class DurationType(models.TextChoices):
        YEAR = "Year", "Year"
        MONTH = "Month", "Month"
        
    code = models.CharField(
        max_length=20, 
        verbose_name='Course Code'
        )
    title = models.CharField(
        max_length=200,
        verbose_name='Course Title'
    ) 
    qualification_level = models.CharField(
        max_length=50,
        choices=QLevel.choices,
        default=QLevel.CERT,
    )
    description = models.TextField(
        verbose_name='Course Description'
    )
 
    campus = models.CharField(
        verbose_name='Campus',
        max_length=10,
        choices=Campus.choices,
        default=Campus.KUK,
    )  
  
    duration_type = models.CharField(
        verbose_name='Duration Type',
        max_length=5, 
        choices=DurationType.choices
    )
    
    duration_length = models.FloatField(
        verbose_name='Duration'
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
