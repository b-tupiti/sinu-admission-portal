/**
 * This script grabs the serialized data (serializedQualifications), loops through
 * each qualification, wraps them in a component, and appends them into the container.
 */

const container = document.getElementById('qualifications-container');


serializedQualifications.forEach(qualification => {
    const qualificationData = extractQualificationData(qualification);
    const component = createDataComponent(qualificationData);
    container.appendChild(component);
});

function extractQualificationData(qualification){
    return {
        'institutionName': qualification.fields.institution_name,
        'course': qualification.fields.course,
        'major': qualification.fields.major,
        'yearStart': qualification.fields.year_start,
        'yearEnd': qualification.fields.year_end,
    }
}

function createDataComponent(data){
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