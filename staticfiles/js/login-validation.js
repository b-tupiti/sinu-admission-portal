const InputVal = {
    EMAIL: false,
    CONFIRMEMAIL: false,
    PASSWORD: false,
    CONFIRMPASS: false,
}

const Input = {
    EMAIL: 'email',
    CONFIRMEMAIL: 'confirmemail',
    PASSWORD: 'password',
    CONFIRMPASS: 'confirmpass',
}

const saveContinueBtn = document.getElementById('save-and-continue');

const passwordRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[#@$!%*?&])[A-Za-z\d#@$!%*?&]{8,}$/;
const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/; 

const email = document.getElementById('email');
const confirmEmail = document.getElementById('confirm-email');
const password = document.getElementById('password');
const confirmPassword = document.getElementById('confirm-password');

const emailIconDiv = document.getElementById('validate-email-check');
const confirmEmailIconDiv = document.getElementById('confirm-email-check');
const passwordIconDiv = document.getElementById('validate-password-check');
const confirmPasswordIconDiv = document.getElementById('confirm-password-check');

email.addEventListener('keyup', function(e){keyEnteredHandler(e.target.value, Input.EMAIL)});
confirmEmail.addEventListener('keyup', function(e){keyEnteredHandler(e.target.value, Input.CONFIRMEMAIL)});
password.addEventListener('keyup', function(e){keyEnteredHandler(e.target.value, Input.PASSWORD)});
confirmPassword.addEventListener('keyup', function(e){keyEnteredHandler(e.target.value, Input.CONFIRMPASS)});


document.addEventListener('DOMContentLoaded', function() { 
    setTimeout(function(){
       loginInit();
    }, 200);
  });


function loginInit(){

    InputVal.PASSWORD = false;
    InputVal.CONFIRMPASS = false;

    if(email.value !== '') {
        InputVal.EMAIL = emailRegex.test(email.value);
        updateIconDiv(InputVal.EMAIL, emailIconDiv);
    }
    if(confirmEmail.value !== ''){
        InputVal.CONFIRMEMAIL = valuesMatch(confirmEmail.value, email.value);
        updateIconDiv(InputVal.CONFIRMEMAIL, confirmEmailIconDiv);
    }

    if(allValidInputs(InputVal))
        saveContinueBtn.removeAttribute('disabled');
    else 
        saveContinueBtn.setAttribute('disabled', true);

}


function keyEnteredHandler(value, inputType){

    switch(inputType){
        
        case 'email':
            InputVal.EMAIL = emailRegex.test(value);
            updateIconDiv(InputVal.EMAIL, emailIconDiv);
            InputVal.CONFIRMEMAIL = valuesMatch(value, confirmEmail.value);
            updateIconDiv(InputVal.CONFIRMEMAIL, confirmEmailIconDiv);
            break;

        case 'confirmemail':
            InputVal.CONFIRMEMAIL = valuesMatch(value, email.value);
            updateIconDiv(InputVal.CONFIRMEMAIL, confirmEmailIconDiv);
            break;

        case 'password':
            InputVal.PASSWORD = passwordRegex.test(value);
            updateIconDiv(InputVal.PASSWORD, passwordIconDiv);
            InputVal.CONFIRMPASS = valuesMatch(value, confirmPassword.value);
            updateIconDiv(InputVal.CONFIRMPASS, confirmPasswordIconDiv);
            break;

        case 'confirmpass':
            InputVal.CONFIRMPASS = valuesMatch(value, password.value);
            updateIconDiv(InputVal.CONFIRMPASS, confirmPasswordIconDiv);
            break;
    }


    if(allValidInputs(InputVal))
        saveContinueBtn.removeAttribute('disabled');
    else 
        saveContinueBtn.setAttribute('disabled', true);


    console.clear();
    console.log(`email: ${email.value}`)
    console.log(`confirm email: ${confirmEmail.value}`)
    console.log(`password: ${password.value}`)
    console.log(`confirm password: ${confirmPassword.value}`)
    console.log(InputVal);

}

function valuesMatch(value, valueToMatch){
    if(value)
        return value === valueToMatch;
    return false;
}


function updateIconDiv(isValid, IconDiv){
    if (isValid){
        IconDiv.innerHTML = `
            <span class="has-text-success ">
                <i class="fa-solid fa-check mr-3"></i>
            </span>`
    }
    else {
        IconDiv.innerHTML = `
            <span class="has-text-danger ">
                <i class="fa-solid fa-x mr-3"></i>
            </span>`
    }
}

function allValidInputs(valInputs){
    let allValid = true;

    Object.keys(valInputs).map(key => {

        if(valInputs[key] == false){
            allValid = false;
            return;
        }

    })

    return allValid;
}


