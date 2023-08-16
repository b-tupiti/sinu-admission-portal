
const form = document.getElementById('application-form');
form.addEventListener('submit', function(event){
    // event.preventDefault();
    appendQualIdsForDeletionToFormData();
});


/**
 * This function attaches a key-value pair that contains the Ids of the 
 * existing qualifications in the database that the user has removed from the DOM,
 * which will then be removed in the database.
 */
function appendQualIdsForDeletionToFormData(){
    // const formData = new FormData(form);
    // console.log(formData);

    if(QUAL_IDS_TO_DELETE.length > 0){
        const serializedIds = JSON.stringify(QUAL_IDS_TO_DELETE);
        const hiddenDeleteIdInput = document.createElement('input');
        hiddenDeleteIdInput.name = 'delete-ids';
        hiddenDeleteIdInput.type ='hidden';
        hiddenDeleteIdInput.value = serializedIds;
        form.append(hiddenDeleteIdInput);
    }

    fetch(`application/${id}/`, {
        method: 'POST',
      })
    
}

