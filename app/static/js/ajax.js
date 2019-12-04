function ajax() {
    var datos = new XMLHttpRequest();
    datos.open("GET","/prueba",true)
    datos.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    datos.onreadystatechange = function() {
     console.log(datos.responseText);
    }
    datos.send();

    var str = JSON.parse(gestorPeticiones.responseText);
    // if (str === "1") {
      //var str2 = "<select>"+"<option value='1'>a</option>"+"<option value='2'>b</option>"+"<option value='3'>c</option>"+"</select>";
    // }
    // ss.innerHTML = str2;  
    ss.innerHTML = "<select>" 
    for (var i in str) {
     ss.innerHTML += "<option value="+str[i].id+">"+str[i].nombre+"</option>";      
    }
    ss.innerHTML += "</select>";
  
}