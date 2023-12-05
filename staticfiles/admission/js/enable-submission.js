document.addEventListener('DOMContentLoaded', function() {
    setTimeout(verifySubmission, 500);
});

const submitBtn = document.getElementById('submit-btn');
const declarationCheckbox = document.getElementById('declaration-checkbox');
const slipInput = document.getElementById('slip-input');
const slipInputName = document.getElementById('slip-input-name');

function verifySubmission(){

    console.log(declarationCheckbox.checked)
    console.log(slipInputName.textContent.trim())
    
    if (declarationCheckbox.checked && slipInputName.textContent.trim() !== '...'){

        
        enableSubmissionButton();
        console.log('verification passed.');

    } 
    else {
        disableSubmissionButton();
        console.log('verification failed.');
    }
}

declarationCheckbox.addEventListener('change', function(){
    setTimeout(verifySubmission, 500);
});

slipInput.addEventListener('change', function(){
    setTimeout(verifySubmission, 500);
});

function enableSubmissionButton(){
    submitBtn.removeAttribute('disabled');
}

function disableSubmissionButton(){
    
    submitBtn.setAttribute('disabled', '');
}