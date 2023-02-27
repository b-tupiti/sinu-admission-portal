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
    photo = models.ImageField()
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
    name = models.CharField(max_length=254, null=True, blank=True)
    file = models.FileField()
    application = models.ForeignKey(Application, on_delete=models.CASCADE, related_name='documents')
    
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)   
    
    def __str__(self):
        return self.id

    