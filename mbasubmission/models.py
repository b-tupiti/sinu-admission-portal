from django.db import models
from django.urls import reverse
import uuid


class Application(models.Model):
    """
    Application model
    """
    class ApplicationState(models.TextChoices):
        PENDING = "PENDING", "PENDING"
        ACCEPTED = "ACCEPTED", "ACCEPTED"
        REJECTED = "REJECTED", "REJECTED"
        
    email = models.EmailField(max_length=254)
    phone_number = models.IntegerField(null=True,blank=True)
    first_name = models.CharField(max_length=254)
    middle_name = models.CharField(max_length=254, null=True, blank=True)
    last_name = models.CharField(max_length=254)
    photo = models.ImageField(upload_to='photos/')
    proposal = models.TextField()
    application_state = models.CharField(max_length=8, choices=ApplicationState.choices, default=ApplicationState.PENDING)
    
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.id
    
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
        return self.id

    