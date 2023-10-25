const container = document.getElementById('qualifications-container');
const addQualBtn = document.getElementById('add-qualification-btn');


/**
 * A handler for when addQualBtn is clicked.
 */
const onClickHander = () => {
    const id = generateNewId();
    const component = createEmptyComponent(id);
    addComponentToContainer(container, component);
}

addQualBtn.addEventListener('click', onClickHander);

//===============================================================//

/**
 * generates a random and temporary id for new qualification.
 * @returns {string}
 */
function generateNewId() {
    const timestamp = new Date().getTime().toString();
    const randomNum = Math.random().toString(36).slice(2, 7); // Adjust length as needed
    return timestamp + randomNum;
}

/**
 * This function creates an empty component and returns it.
 * @returns {HTMLDivElement} a new component
 */
const createEmptyComponent = (id) => {

    const component = document.createElement('div');
    component.setAttribute('id',`qualification_id-${id}`);
    component.setAttribute('class','mt-3 ml-1 mr-1 p-4');
    component.setAttribute('style', 'border: 1px solid rgba(0, 0, 0, 0.1); border-radius: 5px;');


    component.innerHTML = `
    
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
                name="newtq-institution_name-${id}"
                class="input" 
                type="text" 
                placeholder=""
                required
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
                name="newtq-course-${id}"
                class="input" 
                type="text" 
                placeholder=""
                required
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
                name="newtq-year_start-${id}"
                class="input" 
                type="text" 
                placeholder=""
                required
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
                name="newtq-year_end-${id}"
                class="input" 
                type="text" 
                placeholder=""
                required
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
                name="newtq-major-${id}"
                class="input" 
                type="text" 
                placeholder=""
                required
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
                    <input class="file-input" type="file" name="newtqd-certificate-${id}">
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
                    <input class="file-input" type="file" name="newtqd-transcript-${id}">
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

    `
    return component;
}

/**
 * This function takes a container and a component, and appends 
 * and appends the component to the container.
 * @param {HTMLDivElement} container 
 * @param {HTMLDivElement} component 
 */
const addComponentToContainer = (container, component) => {
    container.appendChild(component);
}