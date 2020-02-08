function dia_mes(url) {
  document.getElementById("cards").innerHTML =`
  <div class="column">
  <div class="mes" id="mes">
   date
  </div>
  <hr>
  <div class="Nro_Servicios" id="Nro_servicios">
   0
  </div>
  <a class="" href=""></a>
  <hr>
  <h5>Dias laborados en el mes</h5>
   <div class="dias_laborados" id="dias_laborados">
      <a href=""></a>
   </div>
   
  <hr>
  <h5>saldo servicios</h5>
   <div id="saldo">
      
   </div>
</div>
  `
    let fecha = document.getElementById("fecha_dia").value;
    let dias_laborados = document.getElementById("dias_laborados");
    let saldo_servicios = document.getElementById("saldo");
    let Nro_servicios = document.getElementById("Nro_servicios");
    let nombre_mes = document.getElementById("mes");
    const dia_mes = url + "/mes/" + fecha
    /*const dia_mes = "http://127.0.0.1:5000/mes/" + fecha*/ 
    fetch(dia_mes)
    .then(res => res.json())
    .then(data =>{
       console.log(data)
       let saldo = 0
       let num_servicios = 0
       
       for (var clave in data ){
        // Controlando que json realmente tenga esa propiedad
        if (data.hasOwnProperty(clave)) {
          // Mostrando en pantalla la clave junto a su valor
          let listItem = document.createElement('a');
          listItem.textContent =  data[clave].dia;
          let link = data[clave].url + "/" + "descripcion_servicio" + "/" + data[clave]._id + "/";
          listItem.setAttribute("id", clave); 
          listItem.classList.add("dia_laborado");
          dias_laborados.appendChild(listItem);
          document.getElementById(clave).setAttribute("href",link);
          saldo += data[clave].costo_total
          num_servicios += 1 
          saldo_servicios.textContent = saldo
          Nro_servicios.textContent = num_servicios
          nombre_mes.textContent = `Numero servicios prestados ${data[clave].mes}`
          nombre_mes.textContent.bold()
          
          /*console.log("La clave es " + clave+ " y el valor es " + data[clave].fecha);*/
        }
      }
      
    }) 
    console.log(fecha)
    console.log("esta funcionando");
    dias_laborados.innerHTML=`<p>  </p>`
    
}

function mes_year(url) {
  document.getElementById("cards").innerHTML =`
  <div class="column">
  <div class="mes" id="mes">
   date
  </div>
  <hr>
  <div class="Nro_Servicios" id="Nro_servicios">
   0
  </div>
  <a class="" href=""></a>
  <hr>
  <h5>Dias laborados en el mes</h5>
   <div class="dias_laborados" id="dias_laborados">
      <a href=""></a>
   </div>
   
  <hr>
  <h5>saldo servicios</h5>
   <div id="saldo">
      
   </div>
</div>
  `
    let fecha = document.getElementById("fecha_mes").value;
    let dias_laborados = document.getElementById("dias_laborados");
    let saldo_servicios = document.getElementById("saldo");
    let Nro_servicios = document.getElementById("Nro_servicios");
    let nombre_mes = document.getElementById("mes");
    const dia_mes = url + "/mes_year/" + fecha
    /*const dia_mes = "http://127.0.0.1:5000/mes_year/" + fecha*/
    fetch(dia_mes)
    .then(res => res.json())
    .then(data =>{
       console.log(data)
       let saldo = 0
       let num_servicios = 0
       
       for (var clave in data ){
        // Controlando que json realmente tenga esa propiedad
        if (data.hasOwnProperty(clave)) {
          // Mostrando en pantalla la clave junto a su valor
          let listItem = document.createElement('a');
          listItem.textContent =  data[clave].dia;
          let link = data[clave].url + "/" + "descripcion_servicio" + "/" + data[clave]._id + "/";
          listItem.setAttribute("id", clave); 
          listItem.classList.add("dia_laborado");
          dias_laborados.appendChild(listItem);
          document.getElementById(clave).setAttribute("href",link);
          saldo += data[clave].costo_total
          num_servicios += 1 
          saldo_servicios.textContent = saldo
          Nro_servicios.textContent = num_servicios
          nombre_mes.textContent = `Numero servicios prestados ${data[clave].mes}`
          nombre_mes.textContent.bold()
          
          /*console.log("La clave es " + clave+ " y el valor es " + data[clave].fecha);*/
        }
      }
      
    }) 
    console.log(fecha)
    console.log("esta funcionando");
    dias_laborados.innerHTML=`<p>  </p>`
    
}


