
// this is the variable holding the application.current_section value and is 
// the determinig factor of how the progress bar is rendered.

const currentSection = document.getElementById('current-section').value;
console.log('furthest section reached by user (current): ', currentSection);

const editSection = document.getElementById('edit-section').value;
console.log('section showing on screen (on edit): ', editSection);

init();

function init(){

    let iconWrapperId = null;
    let editIconWrapperId = null;
    let completeIconIds = [];
    let pendingIconIds = [];
    let fullProgressBars = [];
    let disabledIconLinks = [];

    switch(currentSection){
        
        case 'personal_details':
            iconWrapperId = 'pd-icon-wrapper';
            completeIconIds = [];
            pendingIconIds = ['sd-icon-wrapper','eb-icon-wrapper','eh-icon-wrapper','d-icon-wrapper'];
            fullProgressBars = [];
            disabledIconLinks = ['sd-link', 'eb-link', 'eh-link', 'd-link'];
            break;

        case 'sponsor_details':
            iconWrapperId = 'sd-icon-wrapper';
            completeIconIds = ['pd-icon-wrapper'];
            pendingIconIds = ['eb-icon-wrapper','eh-icon-wrapper','d-icon-wrapper'];
            fullProgressBars = ['pdsd-progress'];
            disabledIconLinks = ['eb-link', 'eh-link', 'd-link'];
            break;

        case 'education_background':
            iconWrapperId = 'eb-icon-wrapper';
            completeIconIds = ['pd-icon-wrapper','sd-icon-wrapper'];
            pendingIconIds = ['eh-icon-wrapper','d-icon-wrapper'];
            fullProgressBars = ['pdsd-progress', 'sdeb-progress'];
            disabledIconLinks = ['eh-link', 'd-link'];
            break;

        case 'employment_history':
            iconWrapperId = 'eh-icon-wrapper';
            completeIconIds = ['pd-icon-wrapper','sd-icon-wrapper', 'eb-icon-wrapper'];
            pendingIconIds = ['d-icon-wrapper'];
            fullProgressBars = ['pdsd-progress', 'sdeb-progress', 'ebeh-progress'];
            disabledIconLinks = ['d-link'];
            break;

        case 'declaration':
            iconWrapperId = 'd-icon-wrapper';
            completeIconIds = ['pd-icon-wrapper','sd-icon-wrapper', 'eb-icon-wrapper','eh-icon-wrapper'];
            pendingIconIds = [];
            fullProgressBars = ['pdsd-progress', 'sdeb-progress', 'ebeh-progress','ehd-progress'];
            disabledIconLinks = [];
            break;

        default:
            break;
    }

    switch(editSection){
        case 'personal_details':
            editIconWrapperId = 'pd-icon-wrapper';
            break;

        case 'sponsor_details':
            editIconWrapperId = 'sd-icon-wrapper';
            break;

        case 'education_background':
            editIconWrapperId = 'eb-icon-wrapper';
            break;

        case 'employment_history':
            editIconWrapperId = 'eh-icon-wrapper';
            break;

        case 'declaration':
            editIconWrapperId = 'd-icon-wrapper';
            break;

        default:
            break;
    }

    
    renderCurrentIcon(iconWrapperId);
    renderOnEditIcon(editIconWrapperId);
    renderOtherIcons(completeIconIds, 'complete');
    renderOtherIcons(pendingIconIds, 'pending');
    renderFullProgressBars(fullProgressBars);
    disableIconLinks(disabledIconLinks);
}

// renders full progress bars, by default value of progress element is set to 0 (empty).
// All progress bars left of the current section will be full as the sections progress left to right.
function renderFullProgressBars(barIds){
    barIds.forEach(barId => {
        let progressBar = document.getElementById(barId);
        progressBar.setAttribute('value', 100);
    });
}

// takes in a list of Icon Wrapper Ids, and a status string, and renders the icons
// according to the status i.e. 'complete', 'pending'
function renderOtherIcons(elementIds, status){

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

// renders the icon of the current section accordingly (furthest section reached by user)
function renderCurrentIcon(elementId){
    let iconWrapper = document.getElementById(elementId)
    iconWrapper.classList.add('item-current');
    iconWrapper.innerHTML = '<i class="fa-solid fa-pen-to-square icon-color"></i>';
}

// renders the icon of the section that is on screen
function renderOnEditIcon(elementId){
    let iconWrapper = document.getElementById(elementId)
    iconWrapper.classList.add('on-edit');
}

// disable icon links of sections that are not yet completed
function disableIconLinks(linkIds){
    linkIds.forEach(linkId => {
        let link = document.getElementById(linkId);
        link.removeAttribute('href');
        link.classList.add('disabled-icon-link');
    })
}



