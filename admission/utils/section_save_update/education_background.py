import json
from admission.models.document import DocumentType, HSDocument, HSFormLevel, TQDocument
from admission.models.tertiary_qualification import TertiaryQualification


def save_education_background(request, application):
   
   # Top Section (High Schools)
   
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
   
   # End of Top Section ---------------------------
   
   # extract ids of existing qualifications to delete, if any
   if request.POST.get('delete-ids'):
      ids_of_quals_to_delete: list = json.loads(request.POST.get('delete-ids'))
      for id in ids_of_quals_to_delete:
         try:
            TertiaryQualification.objects.get(id=int(id)).delete()
         except:
            pass
   
   # Existing Tertiary Qualifications, saving changes if any.
   
   existing_tq_data: list[dict] = []
   existing_tqualifications: list = []
   existing_tq_ids: list[int] = []
   
   EXISTING_TERTIARY_QUALIFICATIONS_PREFIX = 'tq-'
   
   for key, values in request.POST.lists():
      
      if str(key).startswith(EXISTING_TERTIARY_QUALIFICATIONS_PREFIX):
         
         tq_id = int(str(key).split('-')[-1])
         
         if tq_id not in existing_tq_ids:
            existing_tq_ids.append(tq_id)
            existing_tqualifications.append({'id': tq_id})
            
         item = {
            'for_tq_id': tq_id,
            'input_name': str(key).split('-')[1],
            'input_value': values
         }
         
         existing_tq_data.append(item)
   
   for qualification in existing_tqualifications:
      for item in existing_tq_data:
         if item['for_tq_id'] == qualification.get('id'):
            qualification.update({'id': qualification.get('id'), item['input_name']: item['input_value'][0]})
            
   for qualification in existing_tqualifications:
      tertiary_qualification = TertiaryQualification.objects.get(id=qualification.get('id'))
      
      tertiary_qualification.institution_name = qualification.get('institution_name')
      tertiary_qualification.course = qualification.get('course')
      tertiary_qualification.year_start = qualification.get('year_start')
      tertiary_qualification.year_end = qualification.get('year_end')
      tertiary_qualification.major = qualification.get('major')
      
      tertiary_qualification.save()
      
   # Existing documents of tertiary qualifications, saving changes if any
   
   EXISTING_TQ_DOCS_PREFIX = 'tqd-'
   for key, values in request.FILES.lists():
      
      if str(key).startswith(EXISTING_TQ_DOCS_PREFIX):
         
         file =  request.FILES.get(key)
         
         tq_id = str(key).split('-')[1]
         document_type = str(key).split('-')[-1]
         print(f'existing tq_id: {tq_id}\ndoc_type: {document_type}')
         
         qualification = TertiaryQualification.objects.get(id=tq_id)
         
         TQDocument.objects.filter(qualification=qualification, document_type=document_type).delete()
         TQDocument.objects.create(qualification=qualification, document_type=document_type, file=file)

   #===========================================================
   
   # New Tertiary Qualifications to be inserted into database.
   
   NEW_TERTIARY_QUALIFICATIONS_PREFIX = 'newtq-'
   
   new_tqualifications: list[dict] = []
   generated_ids: set = set() 
                 
   for key, values in request.POST.lists():
      
      if str(key).startswith(NEW_TERTIARY_QUALIFICATIONS_PREFIX):
         
         # Goes through the list of key-value pairs, and identifies how many qualifications are there.
         # Creates an object per qualification, and appends to list.
         
         generated_id = str(key).split('-')[-1]
         if generated_id not in generated_ids:
            
            data: list[dict] = []
            new_tertiary_qualification_dict = {'id': generated_id, 'data': data}
            new_tqualifications.append(new_tertiary_qualification_dict) 
         
         generated_ids.add(generated_id) 
         
         # Just adds all key-value pairs into an object, and appends it to a list.
         
         input_name = str(key).split('-')[1]
         item_pair: dict = {
            input_name: values[0],
         }
         
         for index, qualification_obj in enumerate(new_tqualifications):
            if qualification_obj.get('id') == generated_id:
               new_tqualifications[index]['data'].append(item_pair)
               break
   
   qualification_id_pairs: list[dict] = []
   for qualification_dict in new_tqualifications:
      
      institution_name = qualification_dict['data'][0]['institution_name']   
      course = qualification_dict['data'][1]['course']   
      year_start = qualification_dict['data'][2]['year_start']   
      year_end = qualification_dict['data'][3]['year_end']   
      major = qualification_dict['data'][4]['major']
      
      new_qualification = TertiaryQualification.objects.create(
         application=application,
         institution_name=institution_name,
         course=course,
         year_start=year_start,
         year_end=year_end,
         major=major
      )
      
      qualification_id_pairs.append({'generated_id': qualification_dict['id'], 'instance_id': new_qualification.id})   
      

   # New Tertiary documents of Qualifications to be inserted into database.
   # e.g. newtqd-certificate-{{item.id}}
   
   NEW_TQ_DOCS_PREFIX = 'newtqd-'
   for key, values in request.FILES.lists():
      
      if str(key).startswith(NEW_TQ_DOCS_PREFIX):
         
         file =  request.FILES.get(key)
         document_type = str(key).split('-')[1]
         id = str(key).split('-')[-1]
         print(id)
         
         try:
            qualification = TertiaryQualification.objects.get(id=id)
         
         except Exception as e:
            print(e)
            for pair in qualification_id_pairs:
               if id == pair['generated_id']:
                  id = pair['instance_id']
                  break
               
            qualification = TertiaryQualification.objects.get(id=id)
               
         TQDocument.objects.create(qualification=qualification, document_type=document_type, file=file)
       
   
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


