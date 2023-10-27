from django.contrib import admin
from .models.application import Application
from .models.document import SponsorshipLetter, HSDocument, TQDocument
from .models.tertiary_qualification import TertiaryQualification
from .models.employment import Employment


class TertiaryQualificationAdmin(admin.ModelAdmin):
    list_display = ('application', 'institution_name', 'course', 'year_start', 'year_end', 'major')
    
admin.site.register(TertiaryQualification, TertiaryQualificationAdmin)


class TQDocumentAdmin(admin.ModelAdmin):
    list_display = ('file', 'qualification', 'document_type')
    
admin.site.register(TQDocument, TQDocumentAdmin)


class HSDocumentAdmin(admin.ModelAdmin):
    list_display = ('file', 'application', 'form_level', 'document_type')

admin.site.register(HSDocument, HSDocumentAdmin)


class SponsorshipLetterAdmin(admin.ModelAdmin):
    list_display = ('file', 'application')

admin.site.register(SponsorshipLetter, SponsorshipLetterAdmin)


class EmploymentAdmin(admin.ModelAdmin):
    list_display = ('firm', 'job_title', 'month_year_started', 'month_year_ended', 'is_current', 'application')

admin.site.register(Employment, EmploymentAdmin)


class ApplicationAdmin(admin.ModelAdmin):
    fieldsets = (
         ('Applicant', {
            'fields': (
                'applicant',
            )
        }),
         ('Course Applying For', {
            'fields': (
                'selected_course',
            )
        }),
        ('Student ID (inserted by applicant if he/she is a former student)', {
            'fields': (
                'student_id',
            )
        }),
        ('Personal Details', {
            'fields': (
                'photo', 
                'title',
                'first_name',
                'middle_name',
                'last_name',
                'date_of_birth',
                'gender',
                'marital_status',
                'phone_number',
                'email',
                'has_special_needs',
            )
        }),
        ('Sponsor Details', {
            'fields': (
                'sponsor_type', 
                'sponsor_name',
                'sponsor_email',
                'sponsor_phone_number',
                'sponsor_address',
            )
        }),
        ('Education Background', {
            'fields': (
                'third_form_school', 
                'third_form_year',
                'fifth_form_school',
                'fifth_form_year',
                'sixth_form_school',
                'sixth_form_year',
                'foundation_school',
                'foundation_year',
            ),
        }),
        ('Declaration', {
            'fields': (
                'is_declared', 
            ),
        }),
        ('Meta', {
            'fields': (
                'edit_section',
                'current_section',
                'application_state', 
            ),
        }),
    )
admin.site.register(Application, ApplicationAdmin)