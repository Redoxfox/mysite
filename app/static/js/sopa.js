function getRndInteger(min, max) {
  return Math.floor(Math.random() * (max - min) ) + min;
}

function coord(x,y) {
    id = "cood_" + x + "-" + y
    let celda = document.getElementById(id);
    let palabra = document.getElementById("palabra");

    value_anterior = palabra.value
    value_letter = celda.innerText
    palabra.value =  value_anterior + value_letter
    console.log(celda)
    console.log(sessionStorage) 
    typeof(sessionStorage)
    if (sessionStorage.length==0) {
        var d = new Date();
        document.getElementById("horas").innerHTML = d.toLocaleTimeString();
        let rbgRojo = getRndInteger(200, 255);
        let rbgVerde = getRndInteger(200, 255);
        let rgbAzul = getRndInteger(200, 255);
        rbgColor = rbgRojo + ","+ rbgVerde + "," + rgbAzul
        celda.style.background = "rgb(" + rbgColor +")";
        localStorage.setItem('rgbColor', rbgColor)
        localStorage.setItem('aciertos', 0)
        //localStorage.Apellido = 'Márquez Montoya'
        var obj = new Object();
        var casilla = x + "-" + y
        obj.value_letter = [value_letter, casilla]
        objSerialized = JSON.stringify(obj);
        sessionStorage.setItem(0 , objSerialized);
        console.log(obj)
    } else {
        var obj = new Object();
        key = sessionStorage.length
        var casilla = x + "-" + y
        obj.value_letter = [value_letter, casilla]
        objSerialized = JSON.stringify(obj);
        sessionStorage.setItem(key, objSerialized);
        let rbgColor = localStorage.getItem('rgbColor')
        celda.style.background = "rgb(" + rbgColor +")";
    }
}

function borrar_palabra(){
  let palabra = document.getElementById("palabra");
  palabra.value = ""
  for (let index = 0; index < sessionStorage.length; index++) {
    let element = sessionStorage.getItem(index);
    let valor_json = JSON.parse(element);
    valor = valor_json.value_letter[1]
    id = "cood_" + valor;
    console.log(id)
    let celda = document.getElementById(id);
    celda.style.background = "white"
  }
  sessionStorage.clear();
  localStorage.clear();
}

function nueva_sopa(){
  let palabra = document.getElementById("palabra");
  palabra.value = ""
  sessionStorage.clear();
  localStorage.clear();
  location.reload(); 
}

function ocultar(id){
  document.getElementById("intrucciones").innerHTML =""
}

function tiempo(){
  var myVar = setInterval(myTimer, 1000);
  function myTimer() {
    var d = new Date();
    document.getElementById("segundos").innerText= myVar;
  } 
}


function intrucciones(){
  document.getElementById("intrucciones").innerHTML =`
    <div class="container_titulo">
      <div id="titulo_instruciones">
        <strong>Instrucciones juego:</strong>
      </div>
      <div id="container_cerrar">
          <div id="cerrar"> X </div>
      </div>
    </div>
              
    <div class="container_instrucciones">
      <p class="instruccion">1. En la sopa de letras hay 15 palabras en ingles.</p>
      <p class="instruccion">2. Las palabras se encuentran distribuidas al azar.</p>
      <p class="instruccion">3. Al dar clic o presionar sobre cada letra cambia de color.</p>
      <p class="instruccion">4. Cuando completes la palabra presiona el boton "Comprobar palabra".</p>
      <p class="instruccion">5. Si la palabra es correcta las letras conservan su color.</p>
      <p class="instruccion">6. Si la palabra es incorrecta las letras volveran a su color original.</p>
      <p class="instruccion">7. Cada que aciertes la palabra cambia de color en las definiciones de la parte inferior.</p>
      <p class="instruccion">8. Si te equivocas en la secuencia de letras presiona el boton "Borrar palabra".</p>
      <p class="instruccion">9. Si deseas cambiar de sopa de letras presiona el boton "Nueva sopa".</p>
    </div>

    <div class="container_titulo">
        <div id="titulo_instruciones">
          <strong>Diviertete!!...</strong>
        </div>
      
    </div>
  `
}

function comprobar_palabra(){

const url = window.origin + "/palabra/";

/* var name = document.getElementById("name");
var message = document.getElementById("message"); */
var obj = {}
for (let index = 0; index < sessionStorage.length; index++) {
  let element = sessionStorage.getItem(index);
  let valor_json = JSON.parse(element);
  obj[index] = valor_json.value_letter[1]
}
console.log(obj)
let palabra = document.getElementById("palabra"); 
let nro_crucigrama = document.getElementById("Nro_crucigrama");
var entry = {
  palabra: palabra.value,
  coordenadas: obj,
  nro_crucigrama : nro_crucigrama.innerText
};

fetch(url, {
  method: "POST",
  credentials: "include",
  body: JSON.stringify(entry),
  cache: "no-cache",
  headers: new Headers({
    "content-type": "application/json"
  })
})
  .then(function (response) {
    if (response.status !== 200) {
      console.log(`Looks like there was a problem. Status code: ${response.status}`);
      return;
    }
    response.json().then(function (data) {
      acierto = data.acierto
      console.log(data)
      var coordenadas = data.coordenadas
      if (acierto) {
        //console.log(data.palabra)
  
        let id_aciertos = document.getElementById("aciertos");
        let id_faltan = document.getElementById("faltan");
        //let cp = id_aciertos.match(patron_aciertos)
        //console.log(patron_aciertos)
        numero_aciertos = parseInt(id_aciertos.innerText) + 1
        faltan = 15 - numero_aciertos
        id_aciertos.innerText =  numero_aciertos
        id_faltan.innerText =  faltan
        
        let idpalabra = data.palabra
        palabra_english = document.getElementById(idpalabra);
        palabra_english.style.textDecoration = "line-through"
        palabra_english.style.background = "green"
        let palabra = document.getElementById("palabra");
        palabra.value = ""
        console.log(Object.values(coordenadas))
        sessionStorage.clear();
        localStorage.clear();
        for (let values of Object.values(coordenadas)) {
          id = "cood_" + values;
          let celda = document.getElementById(id);
          celda.removeAttribute("onclick")
        }
        if (numero_aciertos==15) {
          alert("Felicitaciones has terminado con exito!!!...")
        }
      } else {
        let palabra = document.getElementById("palabra");
        palabra.value = ""
        for (let values of Object.values(coordenadas)) {
          id = "cood_" + values;
          let celda = document.getElementById(id);
          celda.style.background = "white"
        }
        sessionStorage.clear();
        localStorage.clear();
      }
    });
  })
  .catch(function (error) {
    console.log("Fetch error: " + error);
  });
}