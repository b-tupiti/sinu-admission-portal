const container = document.getElementById('items-container');

/// ////////////////
/// Key-value Pairs

const AddButtons = {
    ADD_QUALIFICATION: 'add-qualification-btn',
    ADD_EMPLOYMENT: 'add-prevemp-btn',
}

const ItemType = {
    QUALIFICATION: 'qualification',
    EMPLOYMENT: 'employment',
}

/// /////////////////////
/// Add Functions: Definitions

/**
 * Generates a random temporary ID for new item.
 * @returns {string}
 */
function generateNewId() {
    const timestamp = new Date().getTime().toString();
    const randomNum = Math.random().toString(36).slice(2, 7);
    return timestamp + randomNum;
}

/**
 * This function creates an empty component and returns it.
 * @returns {HTMLDivElement} a new component
 */
const createEmptyQualificationComponent = (id) => {

    const component = document.createElement('div');
    component.setAttribute('id',`item_id-${id}`);
    component.setAttribute('class','mt-3 ml-1 mr-1 p-4 has-background-white');
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
 * This function creates an empty component and returns it.
 * @returns {HTMLDivElement} a new component
 */
const createEmptyEmploymentComponent = (id) => {

    const component = document.createElement('div');
    component.setAttribute('id',`item_id-${id}`);
    component.setAttribute('class','mt-3 ml-1 mr-1  p-4 has-background-white');
    component.setAttribute('style', 'border:1px solid rgba(0, 0, 0,.1);border-radius:5px');


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
            <label class="label has-text-weight-normal">Organization</label>
          </div>
          <div class="field-body">
            <div class="field">
              <div class="control">
                <input
                    name="newpe-firm-${id}" 
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
            <label class="label has-text-weight-normal">Job Title</label>
          </div>
          <div class="field-body">
            <div class="field">
              <div class="control">
                <input 
                name="newpe-job_title-${id}" 
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
            <label class="label has-text-weight-normal">month/year started</label>
          </div>
          <div class="field-body">
            <div class="field">
              <div class="control">
                <input 
                name="newpe-month_year_started-${id}" 
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
            <label class="label has-text-weight-normal">month/year ended</label>
          </div>
          <div class="field-body">
            <div class="field">
              <div class="control">
                <input 
                    name="newpe-month_year_ended-${id}" 
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

function addNewItem(itemType){
    
    const id = generateNewId();
    let component = null;

    switch(itemType){

        case ItemType.QUALIFICATION:
            component = createEmptyQualificationComponent(id);
            break;

        case ItemType.EMPLOYMENT:
            component = createEmptyEmploymentComponent(id);
            break;

        default:
            break;
    }
    
    if(component != null)
        addComponentToContainer(container, component);
    else
        console.error('Component is null');
}

function extractButtonId(event){
    let element = event.target;
    let elementId = element.id;
    if (!elementId) {
        while (element && !elementId) {
            element = element.parentElement;
            elementId = element.id;
        }
    }
    return elementId;
}

/// //////////////////////////////
/// DELETE Functions: Definitions 

const qualificationsIdsForDeletion = [];
function getParentComponentId(buttonId){
    let idToDelete = String(buttonId).split('-').pop();
    componentId = `item_id-${idToDelete}`;
    return { idToDelete,  componentId};
}
function removeQualificationFromContainer(idOfComponent){
    component = document.getElementById(idOfComponent);
    container.removeChild(component);
}

function delegateTask(buttonId){

    switch (buttonId) {
        case AddButtons.ADD_QUALIFICATION:
            addNewItem(ItemType.QUALIFICATION);
            break;
        case AddButtons.ADD_EMPLOYMENT:
            addNewItem(ItemType.EMPLOYMENT);
            break;
        default:
            if(buttonId.startsWith('delete-')){
                console.log(buttonId);

                const { idToDelete, componentId } = getParentComponentId(buttonId);
                removeQualificationFromContainer(componentId);
                qualificationsIdsForDeletion.push(idToDelete);
                console.log(qualificationsIdsForDeletion)
            }
            break;
    }
    
}

/// /////////////////////////////
/// Adding 'click' Event Listener to DOM 

function clickEventHandler(event) {

    try {

        const buttonId = extractButtonId(event);
        delegateTask(buttonId); 

    } catch (error){
        console.info(
            `An error occurred in this click event handler.\n\n${error}`,
        );
    }
}
document.addEventListener("click", clickEventHandler);




