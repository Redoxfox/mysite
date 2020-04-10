//Array imagenes 

let images = ['/static/imgs/img_c1.jpg','/static/imgs/img_c2.jpg','/static/imgs/img_c3.jpg','/static/imgs/img_c4.jpg'];

//Elemento para cargar el slider

let slider = document.getElementById("sliderJs");

//Elemento general del slider

let sliderContainer = document.getElementById('slider-container');



slider.style.width = images.length * 100 + "%";



//Elemento carga navegacion

let sliderNav = document.getElementById("sliderNavigation");
sliderNav.style.background = "rgb(27, 27, 27)";

//Variable para saber si el slider esta activo
let active = true;

//Eventos 
sliderNav.addEventListener("click",(e)=>slideImage(e.target.id.slice(-1)));


//Eventos de rato
sliderContainer.addEventListener("mouseover",()=>{
    if(active){
        active = false
    }
});

//Eventos saber si el raton no esta dentro
sliderContainer.addEventListener("mouseout",()=>{
    if(!active ){
        active = true
    }
});

//Dibujar slider navegacion
for (let img in images){
    //console.log(img)
    slider.innerHTML += `<img src="${images[img]}" class="sliderImages" style="width:${100/images.length}%">`;
    sliderNav.innerHTML += `<span class="slider-nav" id="slider-nav-${img}">`;
}

//Variable contador de imagenes
let cont = 0;

//intervalos de tiempo

const startInterval = () => setInterval(counter,2000);

startInterval();

function counter() {
    if(active){
        cont++;
        if(cont>=images.length) cont=0;
        setInterval(slideImage(cont),2000);
        setInterval(setActivate(cont),2000);
        //console.log(cont);
    }
}

function slideImage(id) {
    if (!active && !isNaN(id)) {
        cont=id;
        setActivate(id)
    }
    slider.style.left= '-'+ id + '00%';
}

let navIcons = [...document.getElementsByClassName("slider-nav")];
//console.log(navIcons)
 function setActivate(id) {
   for (let icons in navIcons) {
       if (icons<navIcons.length) {
           if (navIcons[icons].id==="slider-nav-" + id) {
               document.getElementById(navIcons[icons].id).classList.add("slider-nav-active")
           } else {
               document.getElementById(navIcons[icons].id).classList.remove("slider-nav-active")
           }
           
       }
       
       
   }
} 


