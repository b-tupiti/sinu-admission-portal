// grabbing the add button, and the container where components will be added into
const button = document.getElementById('add-qualification-btn');
const qualificationContainer = document.getElementById('qualifications-container');

// defining a callback function for when the button is clicked
const onClickHander = () => {
    addComponentToContainer(qualificationContainer, createNewComponent);
}

// Attaching a click listener to the button, and the callback function.
button.addEventListener('click', onClickHander);

/**
 * This function takes in a container (HTMLDivElement) and a function that
 * returns a component. It adds the component to the container.
 * @param {HTMLDivElement} container 
 * @param {function} createNewComponent 
 */
const addComponentToContainer = (container, createNewComponent) => {
    component = createNewComponent();
    container.appendChild(component);
}

/**
 * This function creates a new component and returns it.
 * @returns {HTMLDivElement} a new component
 */
const createNewComponent = () => {
    const component = document.createElement('div');
    component.innerHTML = `
    <div class=" mt-3 ml-1 mr-1  p-4  " style="border:1px solid rgba(0, 0, 0,.1);border-radius:5px">
                    
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

