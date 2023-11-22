document.addEventListener('change', handlerFileSelect);

function handlerFileSelect(event){
    const selectedFile = event.target.files[0];
    const parent = event.target.parentNode;
    const nameEl = parent.lastElementChild;
    
    nameEl.textContent = selectedFile.name;
    nameEl.classList.add('has-text-sinu-blue');
}