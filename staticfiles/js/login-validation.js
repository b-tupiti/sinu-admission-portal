

// if all inputs are valid, save and continue button will be enabled.
const inputs = {
    'validEmail': false,
    'confirmEmail': false,
    'validPassword': false,
    'confirmPassword': false,
}

const emailInput = document.getElementById('email');
const confirmEmailInput = document.getElementById('confirm-email');
const passwordInput = document.getElementById('password');
const confirmPasswordInput = document.getElementById('confirm-password');
const emailInfo = document.getElementById('validate-email-check');
const passwordInfo = document.getElementById('validate-password-check')
const confirmEmailInfo = document.getElementById('confirm-email-check');;
const confirmPasswordInfo = document.getElementById('confirm-password-check');


document.addEventListener('DOMContentLoaded', function() {
    if(emailInput.value != '')
        emailValidityCheck(emailInput.value);
    if(confirmEmailInput.value != '')
        confirmEmailCheck(confirmEmailInput.value, emailInput.value);
});

emailInput.addEventListener('keyup', function(){

    emailValidityCheck(this.value);
    
    if(confirmEmailInput.value)
        confirmEmailCheck(this.value, confirmEmailInput.value);
})

confirmEmailInput.addEventListener('keydown', function(e){
    if (e.key === 'Tab' || e.key === 'Enter') {
        return;
    }
    confirmEmailCheck(this.value + e.key, emailInput.value);
});

passwordInput.addEventListener('keyup', function(){
    passwordValidityCheck(this.value);

    if(confirmPasswordInput.value)
        confirmPasswordCheck(this.value, confirmPasswordInput.value);
});

confirmPasswordInput.addEventListener('keydown', function(e){
    if (e.key === 'Tab' || e.key === 'Enter') {
        return;
    }
    confirmPasswordCheck(this.value + e.key, passwordInput.value);
});

document.addEventListener('keydown', function(){
    
    if(allInputsValid())
        document.getElementById('save-and-continue').removeAttribute('disabled');
    else 
        document.getElementById('save-and-continue').setAttribute('disabled', true);
    
});

function allInputsValid(){
    
    let inputValid = true;

    Object.keys(inputs).map(key => {

        if(inputs[key] == false){
            inputValid = false;
            return;
        }

    })

    return inputValid;
}


function passwordValidityCheck(password){
    
    passwordInfo.innerHTML = '';

    res = isValidPassword(password);

    if(res['isValid'] === true){
        passwordInfo.innerHTML = `
        <span class="has-text-success ">
            <i class="fa-solid fa-check mr-3"></i>
        </span>`
        inputs['validPassword'] = true;
    }
    else if (res['isValid'] === false) {
        passwordInfo.innerHTML = `
        <span class="has-text-danger">
            <i class="fa-solid fa-x mr-3"></i>
            <small style="font-size:10px">
            ${res['message']}
            </small>
        </span>`
        inputs['validPassword'] = false;
    }
}

function isValidPassword(password){

    const passwordRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[#@$!%*?&])[A-Za-z\d#@$!%*?&]{8,}$/;

    if (!passwordRegex.test(password)) {
        const requirements = [
            {'rule': /[a-z]/, 'desc': 'at least 1 lower case letter'}, 
            {'rule': /[A-Z]/, 'desc': 'at least 1 upper case letter'}, 
            {'rule': /\d/, 'desc': 'at least 1 numeric value'},   
            {'rule': /[#@$!%*?&]/, 'desc': 'at least one special character (#@$!%*?&)'}, 
            {'rule': /.{8,}/, 'desc': 'at least 8 characters long'}  
        ];

        const message = "Password must meet the following criteria:" +
            requirements.map((requirement) => `${requirement['rule'].test(password) ? '' : requirement['desc']}`);

        return { isValid: false, message: message };
    }

    inputs['validPassword'] = true;
    return { isValid: true, message: "Password is valid." };
}


function emailValidityCheck(email){
    
    emailInfo.innerHTML = '';
    if(isValidEmail(email)){
        emailInfo.innerHTML = `
            <span class="has-text-success ">
                <i class="fa-solid fa-check mr-3"></i>
            </span>`
        inputs['validEmail'] = true;
    }
    else {
        emailInfo.innerHTML = `
            <span class="has-text-danger ">
                <i class="fa-solid fa-x mr-3"></i>
            </span>`
        inputs['validEmail'] = false;
    }
}


function isValidEmail(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
}

function confirmEmailCheck(email, confirmEmail){
    confirmEmailInfo.innerHTML = '';

    if (valuesMatch(email, confirmEmail)){
        confirmEmailInfo.innerHTML = `
        <span class="has-text-success ">
            <i class="fa-solid fa-check mr-3"></i>
        </span>`
        inputs['confirmEmail'] = true;
    }
    else {
        confirmEmailInfo.innerHTML = `
        <span class="has-text-danger ">
            <i class="fa-solid fa-x mr-3"></i>
        </span>`
        inputs['confirmEmail'] = false;
    }
}

function confirmPasswordCheck(password, confirmPassword){
    confirmPasswordInfo.innerHTML = '';

    if (valuesMatch(password, confirmPassword)){
        confirmPasswordInfo.innerHTML = `
        <span class="has-text-success ">
            <i class="fa-solid fa-check mr-3"></i>
        </span>`
        inputs['confirmPassword'] = true;
    }
    else {
        confirmPasswordInfo.innerHTML = `
        <span class="has-text-danger ">
            <i class="fa-solid fa-x mr-3"></i>
        </span>`
        inputs['confirmPassword'] = false;
    }
}

function valuesMatch(value, valueToMatch){
    return value === valueToMatch;
}

