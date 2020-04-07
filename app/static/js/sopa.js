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
        let rbgRojo = getRndInteger(200, 255);
        let rbgVerde = getRndInteger(200, 255);
        let rgbAzul = getRndInteger(200, 255);
        rbgColor = rbgRojo + ","+ rbgVerde + "," + rgbAzul
        celda.style.background = "rgb(" + rbgColor +")";
        localStorage.setItem('rgbColor', rbgColor)
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

    
    /* var obj = new Object();
    obj.name   = name;
    obj.email  = email;
    obj.mobile = mobile;
    obj.note   = note;
    objSerialized = JSON.stringify(obj);
    localStorage.set('hashkey', objSerialized);
    objSerialized = localStorage.get('hashkey');
    obj = JSON.parse(objSerialized);  */
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
var entry = {
  palabra: palabra.value,
  coordenadas: obj
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