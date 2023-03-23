
let activeTab = document.querySelector('#tabs li.is-active');
let activeContent = document.querySelector('#tab-content section.is-active')
  
function change_application_tab(id){

    // remove 'is-active' class from current active tab
    activeTab.classList.remove('is-active');

    // set 'is-active' class to selected tab
    let selectedTab = document.getElementById(id);
    selectedTab.classList.add('is-active');

    // update activeTab variable
    activeTab = selectedTab;

    // Toggle content based on activeTab
    if(activeTab.getAttribute('id') == 'payments_tab'){
        document.getElementById('payments-content').style.display = 'block';
        document.getElementById('details-content').style.display = 'none';
    } else if(activeTab.getAttribute('id') == 'details_tab'){
        document.getElementById('details-content').style.display = 'block';
        document.getElementById('payments-content').style.display = 'none';
    }
}