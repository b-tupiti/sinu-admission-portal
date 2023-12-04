from admission.models.document import TQDocument
from admission.models.employment import Employment
from admission.models.tertiary_qualification import TertiaryQualification
from admission.utils.application_updates import get_tertiary_qualifications
from admission.utils.generators import render_to_pdf


def generate_admission_pdf(application):
    
    t_qualifications = get_tertiary_qualifications(application)
    
    context = {
        'application': application,
        't_qualifications': t_qualifications
    }
    context['current_employment'] = Employment.objects.filter(is_current=True, application=application).first()
    context['previous_employments'] = Employment.objects.filter(is_current=False, application=application)
    
    pdf = render_to_pdf('admission/pdf_templates/admission_form.html', context)
    
    return pdf


    