function getRndInteger(min, max) {
  return Math.floor(Math.random() * (max - min) ) + min;
}

function coord(x,y) {
    let id = "cood_" + x + "-" + y
    let celda = document.getElementById(id);
    let palabra = document.getElementById("palabra");

    let value_anterior = palabra.value
    let value_letter = celda.innerText
    palabra.value =  value_anterior + value_letter
    console.log(celda)
    console.log(sessionStorage) 

    if (sessionStorage.length==0) {
        var hora_ini = new Date().toLocaleTimeString();
        //document.getElementById("horas").innerHTML = d.toLocaleTimeString();
        let rbgRojo = getRndInteger(200, 255);
        let rbgVerde = getRndInteger(200, 255);
        let rgbAzul = getRndInteger(200, 255);
        let rbgColor = rbgRojo + ","+ rbgVerde + "," + rgbAzul
        celda.style.background = "rgb(" + rbgColor +")";
        localStorage.setItem('rgbColor', rbgColor)
        localStorage.setItem('aciertos', 0)
        //localStorage.Apellido = 'Márquez Montoya'
        var obj = new Object();
        var casilla = x + "-" + y
        obj.value_letter = [value_letter, casilla]
        let objSerialized = JSON.stringify(obj);
        sessionStorage.setItem(0 , objSerialized);
        
        let id_faltan = document.getElementById("horas");
        console.log(id_faltan)
        if (id_faltan.textContent==" ") {
          tiempo(hora_ini)
        }
        
        //console.log(xx)
    } else {
        var obj = new Object();
        let key = sessionStorage.length
        var casilla = x + "-" + y
        obj.value_letter = [value_letter, casilla]
        let objSerialized = JSON.stringify(obj);
        sessionStorage.setItem(key, objSerialized);
        let rbgColor = localStorage.getItem('rgbColor')
        celda.style.background = "rgb(" + rbgColor +")";
        //let xx = tiempo()
        //console.log(xx)
    }
}

function borrar_palabra(){
  let palabra = document.getElementById("palabra");
  palabra.value = ""
  for (let index = 0; index < sessionStorage.length; index++) {
    let element = sessionStorage.getItem(index);
    let valor_json = JSON.parse(element);
    let valor = valor_json.value_letter[1]
    let id = "cood_" + valor;
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

function new_soup_topic(id) {
  let url = window.origin
  window.location.href = url + "/blog/sopa_letters/" + id.toString();
}

function tiempo(hora_ini){
  var myVar = setInterval(myTimer, 1000);
  function myTimer() {
     var hora_gactual = new Date().toLocaleTimeString();
     //console.log(typeof(hora_ini));
     let s_hora_ini = hora_ini.split(" ");
     let valor_hora_ini = s_hora_ini[0];
     let split_valor_hora_ini = valor_hora_ini.split(":");
     let s_hora_actual = hora_gactual.split(" ");
     let valor_hora_actual = s_hora_actual[0];
     let split_valor_hora_act = valor_hora_actual.split(":");
     let hora_inicial = parseInt(split_valor_hora_ini[0]);
     let min_inicial = parseInt(split_valor_hora_ini[1]);
     let seg_inicial = parseInt(split_valor_hora_ini[2]);
     let hora_actual = parseInt(split_valor_hora_act[0]);
     let min_actual = parseInt(split_valor_hora_act[1]);
     let seg_actual = parseInt(split_valor_hora_act[2]);
     let total_seg_ini = 0
     let total_seg_act = 0
     let mod_hour = 0
     let mod_min = 0
     let total_seg = 0
     let t_in_horas = 0;
     let t_in_min = 0;
     let t_in_seg = 0;

    //Tiempo cambio(AM-AM)
    if (s_hora_ini[1] == "AM" && s_hora_actual[1] == "AM"){
      total_seg_ini = hora_inicial*3600 + min_inicial*60 + seg_inicial
      total_seg_act = hora_actual*3600 + min_actual*60 + seg_actual
      total_seg = total_seg_act - total_seg_ini 
      if (total_seg < 61) {
        t_in_seg = total_seg
      } else {
        mod_min = total_seg%60
        if (mod_min === 0) {
          t_in_min = total_seg / 60
          t_in_seg = total_seg - t_in_min*60
        } else {
          t_in_min = Math.trunc((total_seg/60))
          t_in_seg = total_seg - t_in_min*60
        }
        mod_hour = total_seg%3600
        if (mod_hour === 0) {
          t_in_horas = total_seg / 3600
        } else {
          t_in_horas = Math.trunc((total_seg/3600))
        }

      }
    }

  //Tiempo cambio(AM-PM)
  if (s_hora_ini[1] == "AM" && s_hora_actual[1] == "PM"){
    total_seg_ini = hora_inicial*3600 + min_inicial*60 + seg_inicial
    total_seg_act = (12+hora_actual)*3600 + min_actual*60 + seg_actual
    total_seg = total_seg_act - total_seg_ini 
    if (total_seg < 61) {
      t_in_seg = total_seg
    } else {
      mod_min = total_seg%60
      if (mod_min === 0) {
        t_in_min = total_seg / 60
        t_in_seg = total_seg - t_in_min*60
      } else {
        t_in_min = Math.trunc((total_seg/60))
        t_in_seg = total_seg - t_in_min*60
      }
      mod_hour = total_seg%3600
      if (mod_hour === 0) {
        t_in_horas = total_seg / 3600
      } else {
        t_in_horas = Math.trunc((total_seg/3600))
      }
    }
  }
     
    //Tiempo cambio (PM-PM)
     if (s_hora_ini[1] == "PM" && s_hora_actual[1] == "PM"){
        total_seg_ini = (12+hora_inicial)*3600 + min_inicial*60 + seg_inicial
        total_seg_act = (12+hora_actual)*3600 + min_actual*60 + seg_actual
        total_seg = total_seg_act - total_seg_ini 
        if (total_seg < 61) {
          t_in_seg = total_seg
        } else {
          mod_min = total_seg%60
          if (mod_min === 0) {
            t_in_min = total_seg / 60
            t_in_seg = total_seg - t_in_min*60
          } else {
            t_in_min = Math.trunc((total_seg/60))
            t_in_seg = total_seg - t_in_min*60
          }
          mod_hour = total_seg%3600
          if (mod_hour === 0 ) {
            t_in_horas = total_seg / 3600
            t_in_min = total_seg - t_in_horas*60
          } else {
            t_in_horas = Math.trunc((total_seg/3600))
          }

        }

     }

     //Tiempo cambio (PM-AM)
     if (s_hora_ini[1] == "PM" && s_hora_actual[1] == "AM"){
        total_seg_ini = (12+hora_inicial)*3600 + min_inicial*60 + seg_inicial
        total_seg_act = hora_actual*3600 + min_actual*60 + seg_actual
        total_seg = total_seg_act - total_seg_ini 
        if (total_seg < 61) {
          t_in_seg = total_seg
        } else {
          mod_min = total_seg%60
          if (mod_min === 0) {
            t_in_min = total_seg / 60
            t_in_seg = total_seg - t_in_min*60
          } else {
            t_in_min = Math.trunc((total_seg/60))
            t_in_seg = total_seg - t_in_min*60
          }
          mod_hour = total_seg%3600
          if (mod_hour === 0) {
            t_in_horas = total_seg / 3600
          } else {
            t_in_horas = Math.trunc((total_seg/3600))
          }
        }
     }


     let d = t_in_horas.toString() + ":" + t_in_min.toString() + ":" + t_in_seg.toString()
     document.getElementById("horas").innerHTML = d;
     return d
  } 
  return myVar;
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
      let acierto = data.acierto
      console.log(data)
      var coordenadas = data.coordenadas
      if (acierto) {
        //console.log(data.palabra)
  
        let id_aciertos = document.getElementById("aciertos");
        let id_faltan = document.getElementById("faltan");
        //let cp = id_aciertos.match(patron_aciertos)
        //console.log(patron_aciertos)
        let numero_aciertos = parseInt(id_aciertos.innerText) + 1
        let faltan = 15 - numero_aciertos
        id_aciertos.innerText =  numero_aciertos
        id_faltan.innerText =  faltan
        
        let idpalabra = data.palabra
        let palabra_english = document.getElementById(idpalabra);
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
