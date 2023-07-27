/**
 * render-progress-bar.js
 * 
 * This script renders the progress bar according to two values:
 * 1. application.edit_section
 * 2. application.current_section
 * 
 * Both values are recieved from an Application instance from the
 * backend, and wrapped inside hidden input elements, which this
 * script retrieves.
 */


// grabbing instance (Application) values - application.current_section, application.edit_section.
const currentSection = document.getElementById('current-section').value;
const editSection = document.getElementById('edit-section').value;

init();

function init() {

    // determining and rendering progress bar elements based on currentSection i.e. application.current_section

    let currentIconId = null;
    let completeIconIds = [];
    let pendingIconIds = [];
    let filledDividersIds = [];

    switch(currentSection){
        
        case 'personal_details':
            currentIconId = 'pd-icon-wrapper';
            completeIconIds = [];
            pendingIconIds = ['sd-icon-wrapper','eb-icon-wrapper','eh-icon-wrapper','d-icon-wrapper'];
            filledDividersIds = [];
            break;

        case 'sponsor_details':
            currentIconId = 'sd-icon-wrapper';
            completeIconIds = ['pd-icon-wrapper'];
            pendingIconIds = ['eb-icon-wrapper','eh-icon-wrapper','d-icon-wrapper'];
            filledDividersIds = ['pdsd-progress'];
            break;

        case 'education_background':
            currentIconId = 'eb-icon-wrapper';
            completeIconIds = ['pd-icon-wrapper','sd-icon-wrapper'];
            pendingIconIds = ['eh-icon-wrapper','d-icon-wrapper'];
            filledDividersIds = ['pdsd-progress', 'sdeb-progress'];
            break;

        case 'employment_history':
            currentIconId = 'eh-icon-wrapper';
            completeIconIds = ['pd-icon-wrapper','sd-icon-wrapper', 'eb-icon-wrapper'];
            pendingIconIds = ['d-icon-wrapper'];
            filledDividersIds = ['pdsd-progress', 'sdeb-progress', 'ebeh-progress'];
            break;

        case 'declaration':
            currentIconId = 'd-icon-wrapper';
            completeIconIds = ['pd-icon-wrapper','sd-icon-wrapper', 'eb-icon-wrapper','eh-icon-wrapper'];
            pendingIconIds = [];
            filledDividersIds = ['pdsd-progress', 'sdeb-progress', 'ebeh-progress','ehd-progress'];
            break;

        default:
            break;
    }

    renderCurrentIcon(document.getElementById(currentIconId));
    renderCompletedSectionIcons(getElementsByIDs(completeIconIds));
    renderPendingSectionIcons(getElementsByIDs(pendingIconIds));
    renderFilledDividers(getElementsByIDs(filledDividersIds));

    // determining and rendering edit icon based on editSection i.e. application.edit_section

    let editIconId = null;

    switch(editSection){
        case 'personal_details':
            editIconId = 'pd-icon-wrapper';
            break;

        case 'sponsor_details':
            editIconId = 'sd-icon-wrapper';
            break;

        case 'education_background':
            editIconId = 'eb-icon-wrapper';
            break;

        case 'employment_history':
            editIconId = 'eh-icon-wrapper';
            break;

        case 'declaration':
            editIconId = 'd-icon-wrapper';
            break;

        default:
            break;
    }
    
    renderEditIcon(document.getElementById(editIconId));
}


/**
 * This function takes an array of Ids and returns an array
 * of their corresponding HTMLElement objects.
 * @param {[]} Ids 
 * @returns {[HTMLElement]}
 */
function getElementsByIDs(Ids){
    const elements = [];
    Ids.forEach(id => {
        elements.push(document.getElementById(id));
    });
    return elements;
}


/**
 * This function takes an array of dividers (HTMLProgressElement) and
 * renders them as filled, indicating that the step is complete.
 * @param {[HTMLProgressElement]} dividers 
 */
function renderFilledDividers(dividers) {
    dividers.forEach(divider => {
        divider.setAttribute('value', 100);
    });
}


/**
 * This function takes an array of icon links (HTMLProgressElement) and
 * disables them.
 * @param {[HTMLAnchorElement]} dividers 
 */
function renderDisabledSectionIcons(icons) {
    icons.forEach(icon => {
        icon.removeAttribute('href');
        icon.classList.add('disabled-icon-link');
    })
}


/**
 * This function takes a section icon and renders it as the current icon.
 * i.e. The furthest section the application is currently at.
 * @param {HTMLAnchorElement} icon 
 */
function renderCurrentIcon(icon) {
    icon.classList.add('item-current');
    icon.innerHTML = '<i class="fa-solid fa-pen-to-square icon-color"></i>';
}


/**
 * This function takes a section icon and renders it as the edit icon.
 * i.e. The section that is on display to the user, currently available for editing.
 * @param {HTMLAnchorElement} icon 
 */
function renderEditIcon(icon) {
    icon.classList.add('on-edit');
}


// This function takes in a list of Icon Wrapper Ids, and a status string, and renders the icons
// according to the status i.e. 'complete', 'pending'
function renderOtherIcons(elementIds, status) {

    if (status == 'complete'){
        elementIds.forEach(elementId => {
            let iconWrapper = document.getElementById(elementId)
            iconWrapper.classList.add('item-complete');
            iconWrapper.innerHTML = '<i class="fa-solid fa-check icon-color"></i>';
        });
    }
    else if (status == 'pending'){
        elementIds.forEach(elementId => {
            let iconWrapper = document.getElementById(elementId)
            iconWrapper.classList.add('item-pending');
            iconWrapper.innerHTML = '<i class="fa-solid fa-ban icon-color"></i>';
        });
    }
}


/**
 * This function renders the sections that are complete.
 * @param {*} icons 
 */
function renderCompletedSectionIcons(icons){
    icons.forEach(icon => {
        icon.classList.add('item-complete');
        icon.innerHTML = '<i class="fa-solid fa-check icon-color"></i>';
    });
}


/**
 * This function renders the sections that are pending.
 * @param {*} icons 
 */
function renderPendingSectionIcons(icons){
    icons.forEach(icon => {
        icon.classList.add('item-pending');
        icon.innerHTML = '<i class="fa-solid fa-ban icon-color"></i>';
        disableIconLink(icon);
    });
}


/**
 * Disables icon link
 * @param {*} icon 
 */
function disableIconLink(icon){
    const link = icon.closest('button');
    link.removeAttribute('href');
    link.classList.add('disabled-icon-link');
}