import json
from admission.models.document import DocumentType, HSDocument, HSFormLevel, TQDocument
from admission.models.tertiary_qualification import TertiaryQualification
from admission.utils.request_helpers import param_not_found_or_empty


def add_new_qualifications_if_given(request, application):

   # grabbing all fields where the name starts with 'new', indicating a new field input.
   fields_list = [
      (str(key), request.POST[key]) for key in request.POST.keys() if key.startswith('new')]
   
   # checking if fields_list is not empty, if it is, it means no new qualifications were added.
   if len(fields_list) > 0:
      
      # grouping all fields that has the same id attached to its name, 
      # indicating belonging to a single qualification instance
      unique_ids = []
      grouped_fields = dict()

      for field_item in fields_list:
         id = field_item[0].split('-')[-1] 
         
         if id not in unique_ids:
            unique_ids.append(id)
            grouped_fields[id] = []
            grouped_fields[id].append(field_item)
            
         else:
            grouped_fields[id].append(field_item)

      
      files_list = [
      (str(key), request.FILES[key]) for key in request.FILES.keys() if key.startswith('new')]
      
      for file in files_list:
         key = file[0].split('-')[-1]
         grouped_fields[key].append(file)
      
      #debug
      # for key, value in grouped_fields.items():
      #    print(f'{key}: {value}')
      #    print('---------------')
         
      
      # looping through the grouped fields and creating an instance of each one in the database
      for group in list(grouped_fields.values()):
         qual_dict = dict()
         
         for field_item in group:
            key = str(field_item[0]).split('-')[-2]
            qual_dict[key] = field_item[1]
         
         print(f'this is the qual dict: {qual_dict}')
         
         qualification = TertiaryQualification.objects.create(
            application=application,
            institution_name=qual_dict['institution'],
            course=qual_dict['course'],
            year_start=qual_dict['year_started'],
            year_end=qual_dict['year_ended'],
            major=qual_dict['major'],
         )

         transcript = qual_dict.get('tertiary_transcript')
         certificate = qual_dict.get('tertiary_certificate')
         
         TQDocument.objects.create(
            file=transcript,
            qualification=qualification,
            document_type=DocumentType.TRANSCRIPT,
         )
         
         TQDocument.objects.create(
            file=certificate,
            qualification=qualification,
            document_type=DocumentType.CERTIFICATE,
         )


def save_education_background(request, application):
   
   delete_qualifications_if_stated(request)
   add_new_qualifications_if_given(request, application)
    
   # form 3 documents
   if request.FILES.get('form_3_certificate'):
      file = request.FILES.get('form_3_certificate')          
      _save_or_replace_document(file, application, DocumentType.CERTIFICATE, HSFormLevel.FORM_3)
      
   if request.FILES.get('form_3_transcript'):
      file = request.FILES.get('form_3_transcript')          
      _save_or_replace_document(file, application, DocumentType.TRANSCRIPT, HSFormLevel.FORM_3)
   
   # form 5 documents  
   if request.FILES.get('form_5_certificate'):
      file = request.FILES.get('form_5_certificate')          
      _save_or_replace_document(file, application, DocumentType.CERTIFICATE, HSFormLevel.FORM_5)
      
   if request.FILES.get('form_5_transcript'):
      file = request.FILES.get('form_5_transcript')          
      _save_or_replace_document(file, application, DocumentType.TRANSCRIPT, HSFormLevel.FORM_5)
      
   # form 6 documents  
   if request.FILES.get('form_6_certificate'):
      file = request.FILES.get('form_6_certificate')          
      _save_or_replace_document(file, application, DocumentType.CERTIFICATE, HSFormLevel.FORM_6)
      
   if request.FILES.get('form_6_transcript'):
      file = request.FILES.get('form_6_transcript')          
      _save_or_replace_document(file, application, DocumentType.TRANSCRIPT, HSFormLevel.FORM_6)
      
   # foundation documents  
   if request.FILES.get('foundation_certificate'):
      file = request.FILES.get('foundation_certificate')          
      _save_or_replace_document(file, application, DocumentType.CERTIFICATE, HSFormLevel.FOUNDATION)
      
   if request.FILES.get('foundation_transcript'):
      file = request.FILES.get('foundation_transcript')          
      _save_or_replace_document(file, application, DocumentType.TRANSCRIPT, HSFormLevel.FOUNDATION)
      
   application.third_form_school = request.POST.get('third_form_school')
   application.third_form_year = request.POST.get('third_form_year')
   application.fifth_form_school = request.POST.get('fifth_form_school')
   application.fifth_form_year = request.POST.get('fifth_form_year')
   application.sixth_form_school = request.POST.get('sixth_form_school')
   application.sixth_form_year = request.POST.get('sixth_form_year')
   application.foundation_school = request.POST.get('foundation_school')
   application.foundation_year = request.POST.get('foundation_year')
   application.save()


def _save_or_replace_document(file, application, document_type, form_level):
        
    document = HSDocument.objects.filter(
            application=application,
            form_level=form_level, 
            document_type=document_type
            )
    
    if document.exists():
        document.delete()
        print('document exists already, deleting it, ready for replacement.')
    
    document = HSDocument(
        file=file,
        application=application,
        form_level=form_level, 
        document_type=document_type
    )
    
    document.save()


def delete_qualifications_if_stated(request):
   # deletes the tertiary qualifications selected by the user, if there is any.
    if not param_not_found_or_empty(request.POST.get('delete-ids')):
        deleteIds = json.loads(request.POST.get('delete-ids'))
        for id in deleteIds:
            TertiaryQualification.objects.get(id=id).delete()