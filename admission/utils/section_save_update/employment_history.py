from admission.models.employment import Employment
import json

def save_employment_history(request, application):
    
    firm = request.POST.get('current-firm')
    job_title = request.POST.get('current-job_title')
    month_year_started = request.POST.get('current-month_year_started')
    
    current_employment = [firm, job_title, month_year_started]
    
    is_complete = True
    for field in current_employment:
        if field is None or field == '':
            is_complete = False
            break
    
    if is_complete:
        
        updated_values = {
            'firm': firm, 
            'month_year_started': month_year_started, 
            'job_title': job_title
        }
        
        Employment.objects.update_or_create(
            application=application,
            month_year_ended=None,
            is_current=True,
            defaults=updated_values
        )
    
    
    # extract ids of existing qualifications to delete, if any
    if request.POST.get('delete-ids'):
        ids_of_quals_to_delete: list = json.loads(request.POST.get('delete-ids'))
        print(ids_of_quals_to_delete)
        for id in ids_of_quals_to_delete:
            try:
                Employment.objects.get(id=int(id)).delete()
            except:
                pass
    else:
        print('no object named delete-ids')
       
    # New Employment records of application
    
    NEW_PREV_EMPLOYMENT_PREFIX = 'newpe-'
    new_prev_employments: list[dict] = []
    generated_ids: set = set()
    
    for key, values in request.POST.lists():
        
        if str(key).startswith(NEW_PREV_EMPLOYMENT_PREFIX):
            
            generated_id = str(key).split('-')[-1]
            if generated_id not in generated_ids:
            
                data: list[dict] = []
                new_prev_employment_dict = {'id': generated_id, 'data': data}
                new_prev_employments.append(new_prev_employment_dict) 
         
            generated_ids.add(generated_id) 
            
            input_name = str(key).split('-')[1]
            item_pair: dict = {
                input_name: values[0],
            }
         
            for index, obj in enumerate(new_prev_employments):
                if obj.get('id') == generated_id:
                    new_prev_employments[index]['data'].append(item_pair)
                    break
    
    for dict_obj in new_prev_employments:
      
        firm = dict_obj['data'][0]['firm']   
        job_title = dict_obj['data'][1]['job_title']   
        month_year_started = dict_obj['data'][2]['month_year_started']   
        month_year_ended = dict_obj['data'][3]['month_year_ended']   
        
      
        Employment.objects.create(
            application=application,
            firm=firm,
            job_title=job_title,
            month_year_started=month_year_started,
            month_year_ended=month_year_ended,
            is_current=False
        )
        
    