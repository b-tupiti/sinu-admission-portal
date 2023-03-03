
window.addEventListener('load', function() {
    
    document.querySelector('#id_document-TOTAL_FORMS').value = '1'; // resets total forms to 1
    count = document.querySelector('#id_document-TOTAL_FORMS').value; // gets total forms value (value = 1)
    
    let initialChild = document.querySelector('#document-formset-wrapper').lastElementChild; // get child of formset-wrapper
    initialChild.setAttribute('id','form-wrapper-' + count); // setting unique id (1) for first/initial child

    // set the id and name of input field in the initialChild (form-wrapper) to correspond with the count
    let input = initialChild.querySelector('input')
    input.setAttribute('id', 'document-' + count)
    input.setAttribute('name', 'document-' + count)
    let deleteButton = initialChild.querySelector('button');
    deleteButton.addEventListener('click',() =>{
        console.log('cant delete first document.')
    })

    initialChild.querySelector('.filename').setAttribute('id','filename-'+count)
    
    
    input.addEventListener('change', () => {
        let id = input.id.split('-')[1]
        let filenameWrapper = initialChild.querySelector('#filename-'+id);
        let filename = input.value.split('\\')[input.value.split('\\').length - 1]
        filenameWrapper.textContent = filename


         /**remove icon if found */
        let icon = initialChild.querySelector('i')
            if(icon != null){ icon.remove()}

        // check for file type
       let fileType = filename.split('.')[1]
       if(fileType == 'pdf'){
            let icon = document.createElement('i');
            icon.setAttribute('class','fa-solid fa-file-pdf')
            filenameWrapper.parentNode.appendChild(icon);
       }
       else {
            let icon = document.createElement('i');
            icon.setAttribute('class','fa-solid fa-file-word')
            filenameWrapper.parentNode.appendChild(icon);
       }

    });

});



let formsetWrapper = document.querySelector('#document-formset-wrapper'); 

// add listener for click event to #add-document button
document.querySelector('#add-document')
.addEventListener('click', () => {
    
    // get last child element in formsetWrapper. (i.e)
    let lastChild = formsetWrapper.lastElementChild;

    let formsTotal = parseInt(document.querySelector('#id_document-TOTAL_FORMS').value);
    formsTotal += 1; // increment formsTotal to modify newChild (form-wrapper) and its child input element
    document.querySelector('#id_document-TOTAL_FORMS').value = formsTotal.toString() // updates TOTAL_FORMS input value
    
    // clone the last child to a new element
    let newChild = lastChild.cloneNode(true);
    newChild.setAttribute('id','form-wrapper-' + formsTotal);
    newChild.querySelector('.filename').textContent = 'no document selected';
    newChild.querySelector('.filename').setAttribute('id','filename-'+ formsTotal)

    // getting input element from new child
    let input = newChild.querySelector('input')
    input.setAttribute('id','document-' + formsTotal)
    input.setAttribute('name','document-' + formsTotal)
    let deleteButton = newChild.querySelector('button');
    deleteButton.addEventListener('click',() =>{
        newChild.remove();
    })
    
    /**remove icon if found */
    let icon = newChild.querySelector('i')
    if(icon != null){ icon.remove()}
    


    input.addEventListener('change', () => {
        
       let id = input.id.split('-')[1]
       let filenameWrapper = newChild.querySelector('#filename-'+id);
       let filename = input.value.split('\\')[input.value.split('\\').length - 1]
       filenameWrapper.textContent = filename
    
        /**remove icon if found */
        let icon = newChild.querySelector('i')
            if(icon != null){ icon.remove()}


       // check for file type
       let fileType = filename.split('.')[1]
       if(fileType == 'pdf'){
            let icon = document.createElement('i');
            icon.setAttribute('class','fa-solid fa-file-pdf')
            filenameWrapper.parentNode.appendChild(icon);
       }
       else {
            let icon = document.createElement('i');
            icon.setAttribute('class','fa-solid fa-file-word')
            filenameWrapper.parentNode.appendChild(icon);
       }

    });

    formsetWrapper.appendChild(newChild);

})


