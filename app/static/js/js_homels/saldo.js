

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
          nombre_mes.textContent = `Numero servicios prestados ${data[clave].mes}  `
          nombre_mes.textContent.bold()
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


function between_date(url) {
 
    let fecha_ini = document.getElementById("fecha_ini").value;
    let fecha_end = document.getElementById("fecha_end").value;
    let containerCards = document.getElementById("cards")
    containerCards.classList.remove("container")
    containerCards.classList.add("containers")
    

    const day_between = url + "/between_date/" + fecha_ini + "/" + fecha_end + "/"
    /*const dia_mes = "http://127.0.0.1:5000/mes_year/" + fecha*/
    fetch(day_between)
    .then(res => res.json())
    .then(data =>{
       /*console.log(data)*/
       /*console.log("esta funcionando");*/
       var element = document.getElementById("cards");
        while (element.firstChild) {
          element.removeChild(element.firstChild);
        }
       for (let year in data){
         if (data.hasOwnProperty(year)) {
          //  console.log(data[year])
           
           for (let month in data[year]){
            //  console.log(data[year][month])
            if(0 != data[year][month].length){
               let id_mes_card = "mes" + "_" + month + year
               let id_Nro_servicios_card = "Nro_servicios" + "_" + month + year
               let id_dias_laborados_card = "id_dias_laborados" + "_" + month + year
               let id_saldo_card = "saldo" + "_" + month + year
               let listItemcards = document.createElement('div');
               id_cards = month + year
               listItemcards.setAttribute("id", id_cards);
               listItemcards.classList.add("cards_mes"); 
               containerCards.appendChild(listItemcards);
               document.getElementById(id_cards).innerHTML =`
               <div class="column">
               <div class="mes" id=${id_mes_card}>
                date
               </div>
               <hr>
               <div class="Nro_Servicios" id=${id_Nro_servicios_card}>
                0
               </div>
               <a class="" href=""></a>
               <hr>
               <h5>Dias laborados en el mes</h5>
                <div class="dias_laborados" id=${id_dias_laborados_card}>
                   <a href=""></a>
                </div>
                
               <hr>
               <h5>saldo servicios</h5>
                <div id=${id_saldo_card}>
                   
                </div>
             </div>
               `
                let num_servicios = 0
                let saldo = 0
                let dias_laborados = document.getElementById(id_dias_laborados_card);
                let saldo_servicios = document.getElementById(id_saldo_card);
                let Nro_servicios = document.getElementById(id_Nro_servicios_card);
                let nombre_mes = document.getElementById(id_mes_card);
                for (let i = 0; i < data[year][month].length; i++) {
                  // Mostrando en pantalla la clave junto a su valor
                       // Mostrando en pantalla la clave junto a su valor
                  clave = year + month + i     
                  let listItem = document.createElement('a');
                  listItem.textContent =  data[year][month][i].dia;
                  let link = data[year][month][i].url + "/" + "descripcion_servicio" + "/" + data[year][month][i]._id + "/";
                  listItem.setAttribute("id", clave); 
                  listItem.classList.add("dia_laborado");
                  dias_laborados.appendChild(listItem);
                  document.getElementById(clave).setAttribute("href",link);
                  saldo += data[year][month][i].costo_total
                  num_servicios += 1 
                  saldo_servicios.textContent = saldo
                  Nro_servicios.textContent = num_servicios
                  nombre_mes.textContent = `Numero servicios prestados ${data[year][month][i].mes}   ${data[year][month][i].year}`
                  nombre_mes.textContent.bold()
                
                  console.log(data[year][month][i]._id)
                  console.log(data[year][month][i].mes)
                  console.log(data[year][month][i].year)
                }
             } 
           }
         }
       }  
    })  
}


