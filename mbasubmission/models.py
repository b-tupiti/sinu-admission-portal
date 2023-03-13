from django.db import models
from django.urls import reverse
import uuid


class Application(models.Model):
    """
    Application model
    """
    class ApplicationState(models.TextChoices):
        PENDING = "PENDING", "PENDING"
        UNDER_ASSESSMENT = "UNDER_ASSESSMENT", "UNDER_ASSESSMENT"
        OFFER_LETTER_ISSUED = "OFFER_LETTER_ISSUED", "OFFER_LETTER_ISSUED"
        CLEARED_FOR_ENROLLMENT = "CLEARED_FOR_ENROLLMENT", "CLEARED_FOR_ENROLLMENT"
        ENROLLMENT_COMPLETE = "ENROLLMENT_COMPLETE", "ENROLLMENT_COMPLETE"
    
    class Title(models.TextChoices):
        MR = "MR","MR"
        MRS = "MRS","MRS"
        MS = "MS","MS"
        DR = "DR","DR"
    
    class Gender(models.TextChoices):
        MALE = "Male", "Male"
        FEMALE = "Female", "Female"
        
    email = models.EmailField(max_length=254)
    phone_number = models.IntegerField()
    title = models.CharField(max_length=3, choices=Title.choices)
    first_name = models.CharField(max_length=254)
    middle_name = models.CharField(max_length=254, null=True, blank=True)
    last_name = models.CharField(max_length=254)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=6,choices=Gender.choices)
    job_title = models.CharField(max_length=254)
    employer = models.CharField(max_length=254)
    photo = models.ImageField(upload_to='photos/')
    proposal = models.TextField()
    application_state = models.CharField(max_length=40, choices=ApplicationState.choices, default=ApplicationState.PENDING)
    
    created = models.DateTimeField(auto_now_add=True)
    
    @property
    def full_name(self):
        if self.middle_name:
            full_name = '{} {} {}'.format(self.first_name,self.middle_name,self.last_name)
            return full_name
        else:
            full_name = '{} {}'.format(self.first_name,self.last_name)
            return full_name
    
    def __str__(self):
        return str(self.id)
    
    def get_absolute_url(self):
        return reverse("application-detail", kwargs={"pk": self.pk})
 
 
    
class Document(models.Model):
    """
    Document model
    """
    file = models.FileField(upload_to='documents/')
    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)   
    
    def __str__(self):
        filename = self.file.name.split('/')[-1]
        return filename

    