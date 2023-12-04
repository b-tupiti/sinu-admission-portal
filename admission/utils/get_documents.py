from admission.models.document import TQDocument
from admission.models.tertiary_qualification import TertiaryQualification


def get_tertiary_documents(application):
    
    tertiary_qualifications = TertiaryQualification.objects.filter(application=application)
    documents = []
    for qualification in tertiary_qualifications:
        documents.extend(TQDocument.objects.filter(qualification=qualification))
        
    return documents


def get_secondary_documents(application):
    return application.high_school_documents.all()
        
