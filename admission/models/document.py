from django.db import models
import uuid
from .application import Application


class HSFormLevel(models.TextChoices):
    FORM_3 = "form_3", "Form 3"
    FORM_5 = "form_5", "Form 5"
    FORM_6 = "form_6", "Form 6"
    FOUNDATION = "foundation", "Foundation or (Form 7)"


class DocumentType(models.TextChoices):
    TRANSCRIPT = "transcript", "Acadmic Transcript"
    CERTIFICATE = "certificate", "Academic Certificate"
    
    
class Document(models.Model):
    """
    Document model
    """
    
    file = models.FileField(upload_to='documents/')
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)   
    
    class Meta:
        abstract = True
        
    def __str__(self):
        return self.file.name.split('/')[-1]
        
     
class SponsorshipLetter(Document):
    application = models.OneToOneField(Application, related_name="sponsor_letter", on_delete=models.CASCADE)

   
class HSDocument(Document):
    application = models.ForeignKey(
        Application,
        related_name="high_school_documents", 
        on_delete=models.CASCADE
    )
    form_level = models.CharField(
        verbose_name="Form Level",
        max_length=20,
        choices=HSFormLevel.choices,
    )
    document_type = models.CharField(
        verbose_name="Document Type",
        max_length=20,
        choices=DocumentType.choices,
    )