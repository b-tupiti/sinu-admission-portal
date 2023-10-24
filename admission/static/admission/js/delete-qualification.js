let cont = document.getElementById('qualifications-container');

const qualificationsIdsForDeletion = []
function clickEventHandler(event) {

    let elementId = event.target.id;
    
    if (deleteButtonClicked(elementId)){
        const { id_num, componentId } = getParentComponentId(elementId);
        removeQualificationFromContainer(componentId);
        qualificationsIdsForDeletion.push(id_num);
    }
}

document.addEventListener("click", clickEventHandler);


function getParentComponentId(elementId){
    let id_num = String(elementId).split('-').pop();
    componentId = `qualification_id-${id_num}`;
    return { componentId, id_num };
}

function removeQualificationFromContainer(idOfComponent){
    component = document.getElementById(idOfComponent);
    cont.removeChild(component);
}

function deleteButtonClicked(elementId){
    return elementId.toString().startsWith('delete-');
}


const form = document.getElementById('application-form');
form.addEventListener('submit', function(event){
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

    fetch(`application/${id}/`, {
        method: 'POST',
      })
    
}

