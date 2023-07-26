from admission.models.document import HSFormLevel, DocumentType


def add_documents_to_context(documents, application, context):
    form_3_certificate = documents.filter(
        application=application,
        form_level=HSFormLevel.FORM_3,
        document_type=DocumentType.CERTIFICATE
        ).first()
    context['form_3_certificate'] = form_3_certificate
        
    form_3_transcript = documents.filter(
        application=application,
        form_level=HSFormLevel.FORM_3,
        document_type=DocumentType.TRANSCRIPT
        ).first()
    context['form_3_transcript'] = form_3_transcript
        
    form_5_certificate = documents.filter(
        application=application,
        form_level=HSFormLevel.FORM_5,
        document_type=DocumentType.CERTIFICATE
        ).first()
    context['form_5_certificate'] = form_5_certificate
    
    form_5_transcript = documents.filter(
        application=application,
        form_level=HSFormLevel.FORM_5,
        document_type=DocumentType.TRANSCRIPT
        ).first()
    context['form_5_transcript'] = form_5_transcript
        
    form_6_certificate = documents.filter(
        application=application,
        form_level=HSFormLevel.FORM_6,
        document_type=DocumentType.CERTIFICATE
        ).first()
    context['form_6_certificate'] = form_6_certificate
    
    form_6_transcript = documents.filter(
        application=application,
        form_level=HSFormLevel.FORM_6,
        document_type=DocumentType.TRANSCRIPT
        ).first()
    context['form_6_transcript'] = form_6_transcript
    
    foundation_certificate = documents.filter(
        application=application,
        form_level=HSFormLevel.FOUNDATION,
        document_type=DocumentType.CERTIFICATE
        ).first()
    context['foundation_certificate'] = foundation_certificate
    
    foundation_transcript = documents.filter(
        application=application,
        form_level=HSFormLevel.FOUNDATION,
        document_type=DocumentType.TRANSCRIPT
        ).first()
    context['foundation_transcript'] = foundation_transcript
    
    return context