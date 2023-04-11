let photoInput = document.querySelector('#id_photo')
photoInput.addEventListener('change',()=>{
    document.querySelector('#img-name').textContent = photoInput.value.split('\\')[photoInput.value.split('\\').length - 1]
})