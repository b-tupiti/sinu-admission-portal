const helpModalBtn = document.getElementById('help-modal-btn');
const closeModalBtn = document.getElementById('close-modal-btn');
const helpModal = document.getElementById('help-modal');

helpModalBtn.addEventListener('click', function(){
    helpModal.classList.add('is-active');
})

closeModalBtn.addEventListener('click', function(){
    helpModal.classList.remove('is-active');
})