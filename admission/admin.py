from django.contrib import admin
from .models.application import Application, ApplicationStatus
from .models.document import HSDocument, TQDocument
from .models.tertiary_qualification import TertiaryQualification
from .models.employment import Employment
from guardian.admin import GuardedModelAdmin
from guardian.shortcuts import get_objects_for_user
from django.contrib.auth.models import Group


admin.site.site_header = 'SINU Portal'
admin.site.site_title = 'SINU Portal'
admin.site.index_title = 'Admissions'

class TertiaryQualificationAdmin(admin.ModelAdmin):
    list_display = ('application', 'institution_name', 'course', 'year_start', 'year_end', 'major')
    
admin.site.register(TertiaryQualification, TertiaryQualificationAdmin)


class TQDocumentAdmin(admin.ModelAdmin):
    list_display = ('file', 'qualification', 'document_type')
    
admin.site.register(TQDocument, TQDocumentAdmin)


class HSDocumentAdmin(admin.ModelAdmin):
    list_display = ('file', 'application', 'form_level', 'document_type')

admin.site.register(HSDocument, HSDocumentAdmin)


class EmploymentAdmin(admin.ModelAdmin):
    list_display = ('firm', 'job_title', 'month_year_started', 'month_year_ended', 'is_current', 'application')

admin.site.register(Employment, EmploymentAdmin)


@admin.register(Application)
class ApplicationAdmin(GuardedModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'selected_course', 'application_status')
    list_filter = ('application_status', 'selected_course')
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
        ('Personal Details', {
            'fields': (
                'title',
                'first_name',
                'middle_name',
                'last_name',
                'date_of_birth',
                'gender',
                'marital_status',
                'mobile_phone_number',
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
        ('Declaration & Deposit Slip', {
            'fields': (
                'is_declared', 
                'deposit_slip',
            ),
        }),
        ('Finance', {
            'fields': (
                'receipt',
            ),
        }),
        ('Student Administration Services (SAS)', {
            'fields': (
                'student_id',
                'letter_of_offer',
            ),
        }),
        ('Meta', {
            'fields': (
                'current_section',
                'furthest_section',
                'application_status', 
            ),
        }),
    )
    
    def get_fieldsets(self, request, obj=None):
        
        fieldsets = super().get_fieldsets(request, obj)
        
        user_groups = request.user.groups.all()
        finance_group, created = Group.objects.get_or_create(name='Finance')
        sas_group, created = Group.objects.get_or_create(name='SAS (Student Administration Services)')
        
        shared_fieldsets = (
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
                ('Personal Details', {
                    'fields': (
                        'title',
                        'first_name',
                        'middle_name',
                        'last_name',
                        'date_of_birth',
                        'gender',
                        'mobile_phone_number',
                        'email',
                    )
                }),
            )
        
        if finance_group in user_groups:
            fieldsets = (
                ('Sponsor Details', {
                    'fields': (
                        'sponsor_type', 
                        'sponsor_name',
                        'sponsor_email',
                        'sponsor_phone_number',
                        'sponsor_address',
                    )
                }),
                ('STAFF: Please upload confirmation of payment. This will be made available to SAS.', {
                    'fields': (
                        'deposit_slip',
                        'receipt',
                    ),
                }),
            )
            return shared_fieldsets + fieldsets
        
        
        elif sas_group in user_groups:
            fieldsets = (
                ('Declaration', {
                    'fields': (
                        'is_declared', 
                    ),
                }),
                ('STAFF: Please enter student ID and upload offer letter if comfirming admission.', {
                    'fields': (
                        'student_id',
                        'letter_of_offer',
                    ),
                }),
            )
            return shared_fieldsets + fieldsets
        
        return fieldsets
    
    
    
    def get_readonly_fields(self, request, obj=None):
        if obj:  # If the object already exists (editing an existing record)
            read_only_fields = (
                'deposit_slip',
                'applicant', 
                'selected_course',
                'title',
                'first_name',
                'middle_name',
                'last_name',
                'date_of_birth',
                'mobile_phone_number',
                'email',
                'gender',
                'sponsor_type',
                'sponsor_name',
                'sponsor_email',
                'sponsor_address',
                'sponsor_phone_number',
                'is_declared',
            )
            return self.readonly_fields + read_only_fields
        else:  # If creating a new object
            return self.readonly_fields
        
    def has_module_permission(self, request):
        if super().has_module_permission(request):
            return True
        return self.get_model_objects(request).exists()
    
    def get_queryset(self, request):
        if request.user.is_superuser:
            return super().get_queryset(request)
        data = self.get_model_objects(request)
        return data
    
    def get_model_objects(self, request, action=None, klass=None):
        opts = self.opts
        actions = [action] if action else ['view']
        klass = klass if klass else opts.model
        model_name = klass._meta.model_name
        return get_objects_for_user(user=request.user, perms=[f'{perm}_{model_name}' for perm in actions], klass=klass)
    
    def has_permission(self, request, obj, action):
        opts = self.opts
        code_name = f'{action}_{opts.model_name}'
        if obj:
            return request.user.has_perm(f'{opts.app_label}.{code_name}', obj)
        else:
            return True
    
    def has_view_permission(self, request, obj=None):
        return self.has_permission(request, obj, 'view')
    
    def has_change_permission(self, request, obj=None):
        return self.has_permission(request, obj, 'change')
    
    def save_model(self, request, obj, form, change):
        
        update_status = request.POST.get('update_status')
        if update_status != None:
            if update_status == ApplicationStatus.UNDER_ASSESSMENT:
                obj.application_status = ApplicationStatus.UNDER_ASSESSMENT
            elif update_status == ApplicationStatus.APPROVED_AND_OFFER_GRANTED:
                obj.application_status = ApplicationStatus.APPROVED_AND_OFFER_GRANTED
                
        super().save_model(request, obj, form, change)

    

    
    
    
    
    
    

