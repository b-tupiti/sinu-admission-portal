from django.db import models
from django.urls import reverse
import uuid
from users.models.user import User
from courses.models.course import Course

class ApplicationState(models.TextChoices):
        DRAFT = "draft", "Draft"
        SUBMITTED = "Submitted", "Submitted"
        

class Section(models.TextChoices):
    PERSONAL_DETAILS = "personal_details", "Personal Details"
    SPONSOR_DETAILS = "sponsor_details", "Sponsor Details"
    EDUCATION_BACKGROUND = "education_background", "Education Background"
    EMPLOYMENT_HISTORY = "employment_history", "Employment History"
    DECLARATION = "declaration", "Declaration"
    
    
class Application(models.Model):
    
    """Owner"""
    
    applicant = models.ForeignKey(
        User,
        to_field='email',
        on_delete=models.CASCADE,
        related_name='applications'
    )
    
    """Course"""
    
    selected_course = models.ForeignKey(
        Course,
        verbose_name='Selected Course',
        to_field='code',
        on_delete=models.CASCADE,
        related_name='applications'
    )
    
    """PERSONAL Details"""
    
    photo = models.ImageField(
        verbose_name='Photo of Applicant',
        upload_to='photos/',
        null=True,
        blank=True,
    )
    
    student_id = models.IntegerField(
        verbose_name='Student ID',
        unique=True, 
        blank=True, 
        null=True
    )
    
    title = models.CharField(
        verbose_name='Title',
        max_length=3, 
        choices=(('mr', 'Mr'), ('mrs', 'Mrs'),('ms', 'Ms'), ('dr', 'Dr')),
        blank=True,
        null=True,
    )
    
    first_name = models.CharField(
        verbose_name='First Name',
        max_length=254,
        null=True,
        blank=True,
    )
    
    middle_name = models.CharField(
        verbose_name='Middle Name',
        max_length=254, 
        null=True, 
        blank=True
    )
    
    last_name = models.CharField(
        verbose_name='Surname',
        max_length=254,
        null=True,
        blank=True,
    )
    
    date_of_birth = models.DateField(
        verbose_name='Date of Birth',
        null=True,
        blank=True,
    )
    
    gender = models.CharField(
        verbose_name='Gender',
        max_length=6,
        choices=(('male', 'Male'), ('female', 'Female')),
        blank=True,
        null=True,
    )
    
    marital_status = models.CharField(
        max_length=8,
        choices = (('single', 'Single'), ('married', 'Married'),('divorced', 'Divorced'), ('widow', 'Widow')),
        blank=True,
        null=True,
    )
    
    phone_number = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )
    
    email = models.EmailField(
        max_length=254,
        null=True,
        blank=True,
    )
    
    has_special_needs =  models.BooleanField(
        verbose_name='Special Needs / Disability',
        default=False,
    )
    
    """SPONSOR Details"""
    
    sponsor_type = models.CharField(
        max_length=25,
        choices = (
            ('private', 'Private'), 
            ('sponsored', 'Sponsored'),
            ('private_with_concession', 'Private with Concession (staff)'), 
        ),
        blank=True,
        null=True,
    )
    
    sponsor_name = models.CharField(
        verbose_name='Name of Sponsor',
        max_length=255,
        blank=True,
        null=True, 
    )
    
    sponsor_email = models.EmailField(
        verbose_name='Sponsor Email',
        null=True,
        blank=True,
    )
    
    sponsor_phone_number = models.CharField(
        verbose_name='Sponsor Phone Number',
        max_length=255,
        null=True,
        blank=True,
    )
    
    sponsor_address = models.CharField(
        verbose_name='Sponsor Address',
        max_length=255,
        null=True,
        blank=True,
    )
    
    """EDUCATION Background"""
    
    third_form_school = models.CharField(
        verbose_name='Third Form School',
        max_length=255,
        null=True,
        blank=True,
    )
    
    third_form_year = models.IntegerField(
        verbose_name='Year in Third Form',
        null=True,
        blank=True,
    )
    
    fifth_form_school = models.CharField(
        verbose_name='Fifth Form School',
        max_length=255,
        null=True,
        blank=True,
    )
    
    fifth_form_year = models.IntegerField(
        verbose_name='Year in Fifth Form',
        null=True,
        blank=True,
    )
    
    sixth_form_school = models.CharField(
        verbose_name='Sixth Form School',
        max_length=255,
        null=True,
        blank=True,
    )
    
    sixth_form_year = models.IntegerField(
        verbose_name='Year in Sixth Form',
        null=True,
        blank=True,
    )
    
    foundation_school = models.CharField(
        verbose_name='Foundation School',
        max_length=255,
        null=True,
        blank=True,
    )
    
    foundation_year = models.IntegerField(
        verbose_name='Year in Foundation',
        null=True,
        blank=True,
    )
    
    institution = models.CharField(
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
        verbose_name='Year Start',
        null=True,
        blank=True,
    )
    
    year_end = models.IntegerField(
        verbose_name='Year Start',
        null=True,
        blank=True,
    )
    
    major = models.CharField(
        max_length=255,
        verbose_name='Major Field of Study',
        null=True,
        blank=True,
    )
    
    """EMPLOYMENT History"""
    
    current_organization = models.CharField(
        max_length=255,
        verbose_name='Current Organization',
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
    
    """DECLARATION"""
    
    is_declared = models.BooleanField(
        verbose_name='Has been Declared',
        default=False,
    )
    
    """ Application Meta Data """
    
    current_section = models.CharField(
        verbose_name="Current Section (keeps track of the section currently on edit)",
        max_length=40,
        choices=CurrentSection.choices,
        default=CurrentSection.PERSONAL_DETAILS,
    )
    
    application_state = models.CharField(
        verbose_name='State of Application',
        max_length=40, 
        choices=ApplicationState.choices, 
        default=ApplicationState.DRAFT
    )
    
    created = models.DateTimeField(auto_now_add=True)
    last_saved = models.DateTimeField(auto_now=True)
    
    
    @property
    def owner(self):
        return self.applicant
        
    
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
        if self.current_section == 'personal_details':
            return reverse("personal-details", kwargs={"pk": self.pk})
        elif self.current_section == 'sponsor_details':
            return reverse('sponsor-details',kwargs={'pk' : self.pk})
        elif self.current_section == 'education_background':
            return reverse('education-background',kwargs={'pk' : self.pk})
        elif self.current_section == 'employment_history':
            return reverse('employment-history',kwargs={'pk' : self.pk})
        elif self.current_section == 'declaration':
            return reverse('declaration',kwargs={'pk' : self.pk})
 
 
    
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
   
    
class ApplicationToken(models.Model):
    """
    Unique Token for each application. Used for generating URL link to upload receipt.
    """
    application = models.OneToOneField(Application,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False) 
    
    def __str__(self):
        return str(self.id)