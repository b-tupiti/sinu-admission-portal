const container = document.getElementById('qualifications-container');

/**
 * This function takes in a container (HTMLDivElement) and a function that
 * returns a component. It adds the component to the container.
 * @param {HTMLDivElement} container 
 * @param {function} createNewComponent 
 */
const addComponentToContainer = (container, component) => {
    container.appendChild(component);
}

// looping through each object, extracting it, and mounting it to the container. 
serializedQualifications.forEach(qualification => {
    const component = createDataComponent(extractQualificationData(qualification));
    addComponentToContainer(container, component);
    addDeleteEventListener(component, qualification.pk);
});

function extractQualificationData(qualification){
    return {
        'id': qualification.pk,
        'institutionName': qualification.fields.institution_name,
        'course': qualification.fields.course,
        'major': qualification.fields.major,
        'yearStart': qualification.fields.year_start,
        'yearEnd': qualification.fields.year_end,
    }
}


// Adding an empty qualification block
const addQualBtn = document.getElementById('add-qualification-btn');


function generateNewId() {
    const timestamp = new Date().getTime().toString();
    const randomNum = Math.random().toString(36).slice(2, 7); // Adjust length as needed
    return timestamp + randomNum;
}

// defining a callback function for when the button is clicked
const onClickHander = () => {

    // give empty component a random ID
    const id = generateNewId();
    const component = createEmptyComponent(id);
    addComponentToContainer(container, component);
    addDeleteEventListener(component, id);
}


const QUAL_IDS_TO_DELETE = [];
function addDeleteEventListener(component, id){
    
    document.getElementById('delete-' + id).addEventListener('click', ()=>{
        container.removeChild(component); // remove from document

        // check if component comes from backend, if it does, save to array, so that it 
        // its id is sent back to the backend for deletion.
        let componentId = String(component.getAttribute('id'));
        if(componentId.startsWith('qualification')){
            QUAL_IDS_TO_DELETE.push(componentId.split('-')[1]);
        }

        console.log('Qualifications to remove on the backend: ')
        console.log(QUAL_IDS_TO_DELETE);
    })
}


// Attaching a click listener to the button, and the callback function.
addQualBtn.addEventListener('click', onClickHander);


/**
 * This function creates an empty component and returns it.
 * @returns {HTMLDivElement} a new component
 */
const createEmptyComponent = (id) => {
    const component = document.createElement('div');
    component.setAttribute('id',`new-qualification-${id}`);

    component.innerHTML = `
    <div id="new-qualification-${id}" class=" mt-3 ml-1 mr-1  p-4  " style="border:1px solid rgba(0, 0, 0,.1);border-radius:5px">
    
    <button 
        id="delete-${id}"
        type="button"
        class="delete"
        >
    </button>
    
    <div class="columns    is-align-items-center  " >
    
    <div class="column is-one-third">
        <div class="field   ">
        <div class="field-label is-normal mb-2" style="text-align:left">
            <label class="label has-text-weight-normal">Institution</label>
        </div>
        <div class="field-body">
            <div class="field">
            <div class="control">
                <input 
                name="institution-1"
                class="input" 
                type="text" 
                placeholder=""
                >
            </div>
            </div>
        </div>
        </div>
    </div>

    <div class="column ">
        <div class="field   ">
        <div class="field-label is-normal mb-2" style="text-align:left">
            <label class="label has-text-weight-normal">Course</label>
        </div>
        <div class="field-body">
            <div class="field">
            <div class="control">
                <input 
                name="course-1"
                class="input" 
                type="text" 
                placeholder=""
                >
            </div>
            </div>
        </div>
        </div>
    </div>

    <div class="column ">
        <div class="field  ">
        <div class="field-label is-normal mb-2" style="text-align:left">
            <label class="label has-text-weight-normal">Year Started</label>
        </div>
        <div class="field-body">
            <div class="field">
            <div class="control">
                <input 
                name="year-started-1"
                class="input" 
                type="text" 
                placeholder=""
                >
            </div>
            </div>
        </div>
        </div>
    </div>

    <div class="column ">
        <div class="field  ">
        <div class="field-label is-normal mb-2" style="text-align:left">
            <label class="label has-text-weight-normal">Year Ended</label>
        </div>
        <div class="field-body">
            <div class="field">
            <div class="control">
                <input 
                name="year-ended-1"
                class="input" 
                type="text" 
                placeholder=""
                >
            </div>
            </div>
        </div>
        </div>
    </div>


    <div class="column ">
        <div class="field  ">
        <div class="field-label is-normal mb-2" style="text-align:left">
            <label class="label has-text-weight-normal">Major Field of study</label>
        </div>
        <div class="field-body">
            <div class="field">
            <div class="control">
                <input 
                name="major-1"
                class="input" 
                type="text" 
                placeholder=""
                >
            </div>
            </div>
        </div>
        </div>
    </div>


    </div>

    <div class="     columns   " style="border-top:1px dotted rgba(0, 0, 0,.05);">
    
    <h2 class="column m-1 is-one-third" style="width:fit-content">
        Upload files
    </h2>

    <div class="column m-1 is-one-third" style="width:fit-content">
        <div class="field is-horizontal ">
        <div class="field-label is-normal">
            <label class="label has-text-weight-normal is-size-7 " style="color:#8d8d8d">Certificate </label>
        </div>
        <div class="field-body">
            <div class="field">
            <div class="control">
                <div class="file has-name is-small">
                    <label class="file-label">
                    <input class="file-input" type="file" name="tertiary-certificate-1">
                    <span class="file-cta">
                        <span class="file-icon">
                        <i class="fas fa-upload"></i>
                        </span>
                        <span class="file-label">
                        browse 
                        </span>
                    </span>
                    <span class="file-name">
                        ...
                    </span>
                    </label>
                </div>
            </div>
            </div>
        </div>
        </div>
        
    </div>

    <div class="column m-1 is-one-third" style="width:fit-content">
        <div class="field is-horizontal ">
        <div class="field-label is-normal">
            <label class="label has-text-weight-normal is-size-7 " style="color:#8d8d8d">Transcript </label>
        </div>
        <div class="field-body">
            <div class="field">
            <div class="control">
                <div class="file has-name is-small">
                    <label class="file-label">
                    <input class="file-input" type="file" name="tertiary-transcript-1">
                    <span class="file-cta">
                        <span class="file-icon">
                        <i class="fas fa-upload"></i>
                        </span>
                        <span class="file-label">
                        browse 
                        </span>
                    </span>
                    <span class="file-name">
                        ...
                    </span>
                    </label>
                </div>
            </div>
            </div>
        </div>
        </div>
        
    </div>

    </div>

    </div>
    `
    return component;
}


/**
 * This function creates a new data component and returns it.
 * @returns {HTMLDivElement} a data-filled component
 */
function createDataComponent(data){
    const component = document.createElement('div');
    component.setAttribute('id',`qualification-${data.id}`);

    component.innerHTML = `
    <div id="qualification-${data.id}" class="mt-3 ml-1 mr-1  p-4" style="position:relative;border:1px solid rgba(0, 0, 0,.1);border-radius:5px;">
    
    <button 
        id="delete-${data.id}"
        type="button"
        class="delete"
        >
    </button>

    <div class="columns    is-align-items-center  " >
    
    <div class="column is-one-third">
        <div class="field   ">
        <div class="field-label is-normal mb-2" style="text-align:left">
            <label class="label has-text-weight-normal">Institution</label>
        </div>
        <div class="field-body">
            <div class="field">
            <div class="control">
                <input 
                name="institution-1"
                class="input" 
                type="text" 
                value="${data.institutionName}"
                >
            </div>
            </div>
        </div>
        </div>
    </div>

    <div class="column ">
        <div class="field   ">
        <div class="field-label is-normal mb-2" style="text-align:left">
            <label class="label has-text-weight-normal">Course</label>
        </div>
        <div class="field-body">
            <div class="field">
            <div class="control">
                <input 
                name="course-1"
                class="input" 
                type="text" 
                value="${data.course}"
                >
            </div>
            </div>
        </div>
        </div>
    </div>

    <div class="column ">
        <div class="field  ">
        <div class="field-label is-normal mb-2" style="text-align:left">
            <label class="label has-text-weight-normal">Year Started</label>
        </div>
        <div class="field-body">
            <div class="field">
            <div class="control">
                <input 
                name="year-started-1"
                class="input" 
                type="text" 
                value="${data.yearStart}"
                >
            </div>
            </div>
        </div>
        </div>
    </div>

    <div class="column ">
        <div class="field  ">
        <div class="field-label is-normal mb-2" style="text-align:left">
            <label class="label has-text-weight-normal">Year Ended</label>
        </div>
        <div class="field-body">
            <div class="field">
            <div class="control">
                <input 
                name="year-ended-1"
                class="input" 
                type="text" 
                value="${data.yearEnd}"
                >
            </div>
            </div>
        </div>
        </div>
    </div>


    <div class="column ">
        <div class="field  ">
        <div class="field-label is-normal mb-2" style="text-align:left">
            <label class="label has-text-weight-normal">Major Field of study</label>
        </div>
        <div class="field-body">
            <div class="field">
            <div class="control">
                <input 
                name="major-1"
                class="input" 
                type="text" 
                value="${data.major}"
                >
            </div>
            </div>
        </div>
        </div>
    </div>


    </div>

    <div class="     columns   " style="border-top:1px dotted rgba(0, 0, 0,.05);">
    
    <h2 class="column m-1 is-one-third" style="width:fit-content">
        Upload files
    </h2>

    <div class="column m-1 is-one-third" style="width:fit-content">
        <div class="field is-horizontal ">
        <div class="field-label is-normal">
            <label class="label has-text-weight-normal is-size-7 " style="color:#8d8d8d">Certificate </label>
        </div>
        <div class="field-body">
            <div class="field">
            <div class="control">
                <div class="file has-name is-small">
                    <label class="file-label">
                    <input class="file-input" type="file" name="tertiary-certificate-1">
                    <span class="file-cta">
                        <span class="file-icon">
                        <i class="fas fa-upload"></i>
                        </span>
                        <span class="file-label">
                        browse 
                        </span>
                    </span>
                    <span class="file-name">
                        ...
                    </span>
                    </label>
                </div>
            </div>
            </div>
        </div>
        </div>
        
    </div>

    <div class="column m-1 is-one-third" style="width:fit-content">
        <div class="field is-horizontal ">
        <div class="field-label is-normal">
            <label class="label has-text-weight-normal is-size-7 " style="color:#8d8d8d">Transcript </label>
        </div>
        <div class="field-body">
            <div class="field">
            <div class="control">
                <div class="file has-name is-small">
                    <label class="file-label">
                    <input class="file-input" type="file" name="tertiary-transcript-1">
                    <span class="file-cta">
                        <span class="file-icon">
                        <i class="fas fa-upload"></i>
                        </span>
                        <span class="file-label">
                        browse 
                        </span>
                    </span>
                    <span class="file-name">
                        ...
                    </span>
                    </label>
                </div>
            </div>
            </div>
        </div>
        </div>
        
    </div>

    </div>

    </div>
    `

    
    return component;
}



