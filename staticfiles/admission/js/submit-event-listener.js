/// /////////////////////////////
/// Adding 'submit' Event Listener to FORM

const form = document.getElementById('application-form');

form.addEventListener('submit', function(event){
    console.log(qualificationsIdsForDeletion);
    appendQualIdsForDeletionToFormData(qualificationsIdsForDeletion);
});

/**
 * This function attaches a key-value pair that contains the Ids of the 
 * existing qualifications in the database that the user has removed from the DOM,
 * which will then be removed in the database.
 */
function appendQualIdsForDeletionToFormData(qualificationsIdsForDeletion){
    
    if(qualificationsIdsForDeletion.length > 0){
        const qualIdsToDelete = JSON.stringify(qualificationsIdsForDeletion);
        const hiddenDeleteIdInput = document.createElement('input');
        hiddenDeleteIdInput.name = 'delete-ids';
        hiddenDeleteIdInput.type ='hidden';
        hiddenDeleteIdInput.value = qualIdsToDelete;
        form.append(hiddenDeleteIdInput);
    }

    applicationId = document.getElementById('application-id').value
    console.log(applicationId)
    fetch(`/admission/application/${applicationId}/`, {
        method: 'POST',
      })
    
}