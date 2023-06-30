from django.contrib import admin
from .models import Application


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