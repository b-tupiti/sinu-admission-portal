from django.db import models
from users.models.user import User
from courses.models.course import Course
from django.urls import reverse
from django_countries.fields import CountryField

class ApplicationStatus(models.TextChoices):
        DRAFT = "draft", "Draft"
        PENDING_DEPOSIT_VERIFICATION = "pending_deposit_verification", "Pending Deposit Verification"
        UNDER_ASSESSMENT = "under_assessment", "Under Assessment"
        APPROVED_AND_OFFER_GRANTED = "approved_and_offer_granted", "Approved and Offer Granted"
        

class Section(models.TextChoices):
    PERSONAL_DETAILS = "personal_details", "Personal Details"
    SPONSOR_DETAILS = "sponsor_details", "Sponsor Details"
    EDUCATION_BACKGROUND = "education_background", "Education Background"
    EMPLOYMENT_HISTORY = "employment_history", "Employment History"
    DECLARATION = "declaration", "Declaration"

    
class Province(models.TextChoices):
    GUADALCANAL = 'Guadalcanal', 'Guadalcanal'
    WESTERN = 'Western', 'Western'
    TEMOTU = 'Temotu', 'Temotu'
    MALAITA = 'Malaita', 'Malaita'
    ISABEL = 'Isabel', 'Isabel'
    CHOISEUL = 'Choiseul', 'Choiseul'
    MAKIRAULAWA = 'Makira/Ulawa', 'Makira/Ulawa'
    RENBEL = 'Rennell/Bellona', 'Rennell/Bellona'
    CENTRAL = 'Central', 'Central'
    
class MaritalStatus(models.TextChoices):
    SINGLE = 'Single', 'Single'
    MARRIED = 'Married', 'Married'
    DIVORCED = 'Divorced', 'Divorced'
    WIDOW = 'Widow', 'Widow'
 
class Title(models.TextChoices):
    MR = 'Mr', 'Mr'
    MRS = 'Mrs', 'Mrs'
    MS = 'Ms', 'Ms'
    DR = 'Dr', 'Dr'
    
class Gender(models.TextChoices):
    MALE = 'Male', 'Male'
    FEMALE = 'Female', 'Female'
    
class Constituency(models.TextChoices):
    AOKE_LANGALANGA = 'Aoke-Langalanga', 'Aoke-Langalanga'
    BAEGU_ASIFOLA = 'Baegu-Asifola', 'Baegu-Asifola'
    CENTRAL_GUADALCANAL = 'Central Guadalcanal', 'Central Guadalcanal'
    CENTRAL_HONIARA = 'Central Honiara', 'Central Honiara'
    CENTRAL_KWARAE = 'Central Kwara\'ae', 'Central Kwara\'ae'
    CENTRAL_MAKIRA = 'Central Makira', 'Central Makira'
    EAST_AREARE = 'East ꞌAreꞌare', 'East ꞌAreꞌare'
    EAST_CENTRAL_GUADALCANAL = 'East Central Guadalcanal', 'East Central Guadalcanal'
    EAST_CHOISEUL = 'East Choiseul', 'East Choiseul'
    EAST_GUADALCANAL = 'East Guadalcanal', 'East Guadalcanal'
    EAST_HONIARA = 'East Honiara', 'East Honiara'
    EAST_KWAIO = 'East Kwaio', 'East Kwaio'
    EAST_MAKIRA = 'East Makira', 'East Makira'
    EAST_MALAITA = 'East Malaita', 'East Malaita'
    FALEKA = 'Fataleka', 'Fataleka'
    GAO_BUGOTU = 'Gao-Bugotu', 'Gao-Bugotu'
    GIZO_KOLOMBANGARA = 'Gizo-Kolombangara', 'Gizo-Kolombangara'
    HOGRAO_KIA_HAVULEI = 'Hograno-Kia-Havulei', 'Hograno-Kia-Havulei'
    LAU_MBAELELEA = 'Lau Mbaelelea', 'Lau Mbaelelea'
    MALAITA_OUTER_ISLANDS = 'Malaita Outer Islands', 'Malaita Outer Islands'
    MARINGE_KOKOTA = 'Maringe-Kokota', 'Maringe-Kokota'
    MAROVO = 'Marovo', 'Marovo'
    NGGELLA = 'Nggella', 'Nggella'
    NORTH_EAST_GUADALCANAL = 'North East Guadalcanal', 'North East Guadalcanal'
    NORTH_GUADALCANAL = 'North Guadalcanal', 'North Guadalcanal'
    NORTH_MALAITA = 'North Malaita', 'North Malaita'
    NORTH_NEW_GEORGIA = 'North New Georgia', 'North New Georgia'
    NORTH_VELLA_LA_VELLA = 'North Vella La Vella', 'North Vella La Vella'
    NORTH_WEST_CHOISEUL = 'North West Choiseul', 'North West Choiseul'
    NORTH_WEST_GUADALCANAL = 'North West Guadalcanal', 'North West Guadalcanal'
    RANNOGGA_SIMBO = 'Rannogga-Simbo', 'Rannogga-Simbo'
    RENNELL_BELLONA = 'Rennell Bellona', 'Rennell Bellona'
    SAVO_RUSSELLS = 'Savo-Russells', 'Savo-Russells'
    SHORTLANDS = 'Shortlands', 'Shortlands'
    SOUTH_CHOISEUL = 'South Choiseul', 'South Choiseul'
    SOUTH_GUADALCANAL = 'South Guadalcanal', 'South Guadalcanal'
    SMALL_MALAITA = 'Small Malaita', 'Small Malaita'
    SOUTH_NEW_GEORGIA_RENDOVA_TETEPARE = 'South New Georgia-Rendova-Tetepare', 'South New Georgia-Rendova-Tetepare'
    SOUTH_VELLA_LA_VELLA = 'South Vella La Vella', 'South Vella La Vella'
    TEMOTU_NENDE = 'Temotu Nende', 'Temotu Nende'
    TEMOTU_PELE = 'Temotu Pele', 'Temotu Pele'
    TEMOTU_VATUD = 'Temotu Vatud', 'Temotu Vatud'
    UGI_ULAWA = 'Ugi-Ulawa', 'Ugi-Ulawa'
    WEST_AREARE = 'West ꞌAreꞌare', 'West ꞌAreꞌare'
    WEST_GUADALCANAL = 'West Guadalcanal', 'West Guadalcanal'
    WEST_HONIARA = 'West Honiara', 'West Honiara'
    WEST_KWAIO = 'West Kwaio', 'West Kwaio'
    WEST_KWARAE = 'West Kwara\'ae', 'West Kwara\'ae'
    WEST_NEW_GEORGIA_VONA_VONA = 'West New Georgia - Vona Vona', 'West New Georgia - Vona Vona'
    WEST_MAKIRA = 'West Makira', 'West Makira'
    
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
        max_length=10, 
        choices=Title.choices,
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
        choices=Gender.choices,
        blank=True,
        null=True,
    )
    
    marital_status = models.CharField(
        verbose_name='Marital Status',
        max_length=8,
        choices=MaritalStatus.choices,
        blank=True,
        null=True,
    )
    
    province = models.CharField(
        max_length=150,
        choices=Province.choices,
        blank=True,
        null=True,
    )
    
    constituency = models.CharField(
        max_length=255,
        choices=Constituency.choices,
        blank=True,
        null=True,
    )
    
    ward = models.CharField(
        max_length=255,
        choices=Constituency.choices,
        blank=True,
        null=True,
    )
    
    citizenship = CountryField(
        verbose_name='Citizenship',
        blank=True,
        null=True,
    )
    
    country_of_birth = CountryField(
        verbose_name='Country of Birth',
        blank=True,
        null=True,
    )
    
    permanent_address = models.TextField(
        verbose_name='Permanent Address',
        blank=True,
        null=True,
    )
    
    guardian_name = models.CharField(
        verbose_name='Name of Guardian',
        max_length=255,
        blank=True,
        null=True,
    )
    
    guardian_address = models.TextField(
        verbose_name='Guardian Address',
        blank=True,
        null=True,
    )
    
    guardian_phone_number = models.CharField(
        verbose_name='Guardian Phone Number',
        max_length=255,
        blank=True,
        null=True,
    )
    
    contact_postal = models.TextField(
        verbose_name='Contact (Postal)',
        max_length=255,
        blank=True,
        null=True,
    )
    
    mobile_phone_number = models.CharField(
        verbose_name='Mobile Number',
        max_length=100,
        blank=True,
        null=True,
    )
    
    telephone_number = models.CharField(
        verbose_name='Telephone Number',
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
    
    medical_report = models.FileField(
        upload_to='medical/',
        verbose_name='Medical Report',
        null=True,
        blank=True,
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
    
    sponsor_address = models.TextField(
        verbose_name='Sponsor Address',
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
    
    third_form_year = models.CharField(
        verbose_name='Year in Third Form',
        max_length=4,
        null=True,
        blank=True,
    )
    
    fifth_form_school = models.CharField(
        verbose_name='Fifth Form School',
        max_length=255,
        null=True,
        blank=True,
    )
    
    fifth_form_year = models.CharField(
        verbose_name='Year in Fifth Form',
        max_length=4,
        null=True,
        blank=True,
    )
    
    sixth_form_school = models.CharField(
        verbose_name='Sixth Form School',
        max_length=255,
        null=True,
        blank=True,
    )
    
    sixth_form_year = models.CharField(
        verbose_name='Year in Sixth Form',
        max_length=4,
        null=True,
        blank=True,
    )
    
    foundation_school = models.CharField(
        verbose_name='Foundation School',
        max_length=255,
        null=True,
        blank=True,
    )
    
    foundation_year = models.CharField(
        verbose_name='Year in Foundation',
        max_length=4,
        null=True,
        blank=True,
    )
    
    """DECLARATION"""
    
    is_declared = models.BooleanField(
        verbose_name='Has been Declared',
        default=False,
    )
    
    """ FINANCE GROUP """
    
    deposit_slip = models.FileField(
        upload_to='slips/',
        verbose_name='Deposit Slip',
        null=True,
        blank=True,
    )
    
    receipt = models.FileField(
        upload_to='receipts/',
        verbose_name='Receipt',
        null=True,
        blank=True,
    )
    
    """ SAS GROUP """
    
    letter_of_offer = models.FileField(
        upload_to='offer_letters/',
        verbose_name='Letter of Offer',
        null=True,
        blank=True,
    )
    
    """ Application Meta Data """
    
    furthest_section = models.CharField(
        verbose_name="The furthest section that the user has reached.",
        max_length=40,
        choices=Section.choices,
        default=Section.PERSONAL_DETAILS,
    )
    
    current_section = models.CharField(
        verbose_name="The section that is on edit by user (current).",
        max_length=40,
        choices=Section.choices,
        default=Section.PERSONAL_DETAILS,
    )
    
    application_status = models.CharField(
        verbose_name='State of Application',
        max_length=40, 
        choices=ApplicationStatus.choices, 
        default=ApplicationStatus.DRAFT
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
        """_summary_
        goes to the section that the user last reached.
        Returns:
            _type_: _description_
        """
        if self.current_section == Section.PERSONAL_DETAILS:
            self.edit_section = Section.PERSONAL_DETAILS  
            
        elif self.current_section == Section.SPONSOR_DETAILS:
            self.edit_section = Section.SPONSOR_DETAILS
            
        elif self.current_section == Section.EDUCATION_BACKGROUND:
            self.edit_section = Section.EDUCATION_BACKGROUND
            
        elif self.current_section == Section.EMPLOYMENT_HISTORY:
            self.edit_section = Section.EMPLOYMENT_HISTORY
            
        elif self.current_section == Section.DECLARATION:
            self.edit_section = Section.DECLARATION
        
        self.save()
        return reverse('application', kwargs={'pk': self.pk})
 
 
    


    
