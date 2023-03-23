 // function called on buttons with the IDs. The id is used to fetch the parent node and icon
 function toggle_expansion(id){
        
    // the content section will display/hide, the icon will change
    let contentSection = getContentSection(id);
    let icon = document.getElementById(id).getElementsByTagName('i')[0];

    // toggling the two elements
    componentIsExpanded(contentSection) ? 
        expandComponent(contentSection, icon) :
        compressComponent(contentSection, icon);

}

function getContentSection(id){
    
    let parent = document.getElementById(id).closest('section');
    let contentSection = parent.lastElementChild;
    return contentSection;
}

function componentIsExpanded(contentSection){
    return contentSection.classList.contains('is-hidden')
}

function expandComponent(contentSection, icon){
    contentSection.classList.remove('is-hidden')
    icon.setAttribute('class', 'fa-solid fa-minus');
}

function compressComponent(contentSection, icon){
    contentSection.classList.add('is-hidden')
    icon.setAttribute('class', 'fa-solid fa-plus');
}

