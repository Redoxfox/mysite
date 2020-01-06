var servicios = document.getElementById('servicios2');
var navbar2 = document.getElementById('Of_Servicios');

function submenu(){
   navbar2.style.display = 'block';
}

servicios.addEventListener('mouseover', function(e) {
    navbar2.style.display = 'block'; 
})

navbar2.addEventListener('mouseout', function(e) {
        navbar2.style.display = 'none';
})