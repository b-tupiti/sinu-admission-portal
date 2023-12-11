document.addEventListener('DOMContentLoaded', function() {
    
    const saveButton = document.querySelector('input[name="_save"]');
    saveButton.disabled = true;

    try {
        const receiptUpload = document.querySelector('input[name="receipt"]');
        receiptUpload.addEventListener('change', function(){
            saveButton.disabled = false;
        })
    } catch (error) {}
    

    try {
        
        const offerUpload = document.querySelector('input[name="letter_of_offer"]');
        offerUpload.addEventListener('change', function(){
            saveButton.disabled = false;
        })
    } catch (error) {}

});



