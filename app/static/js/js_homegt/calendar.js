function new_move(day, month, year){
    console.log(day, month, year);
    let fecha = year + "-" + month + "-" + day;
    let movimientos = document.getElementById("movimientos");
   
    let listId_movimiento = document.createElement('div');
    id_movimiento = year + month + day
    listId_movimiento.setAttribute("id", id_movimiento);
    listId_movimiento.classList.add("cards_mes"); 
    movimientos.appendChild(listId_movimiento);
    document.getElementById(id_movimiento).innerHTML =`
        <h3 class="logo">Gastos e ingresos personales</h3> 
        <div class="select-move">
            <button  type="button" class="Editar" >Nuevo Ingreso</button> 
            <button  type="button" class="Editar" >Nuevo Gasto</button> 
            <div class="Editar" >${fecha}</div>
            <img class="img_close" src="${window.origin}/static/imgs/error.png">
        </div>
    `
    let containerCards = document.getElementById(id_movimiento)
    
}


function mes_anterior(month, year) {
    let month_actual = month;
    let year_actual = year;
    let month_anterior = month_actual - 1
    let year_anterior = year_actual 
    let month_siguiente = month_actual + 1
    let year_siguiente = year_actual 
    var primer_vacio = []
    var semana_vacio = []

    let meses = ["undefine", "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto",
                "Septiembre","Octubre", "Noviembre", "Diciembre"];
    if (month_anterior==0) {
        month_anterior = 12
        month_actual = 1
        month_siguiente = 2
        year_actual = year
        year_anterior = year-1
        year_siguiente = year
    }


    if (month_siguiente==13) {
        month_anterior = 11
        month_actual = 12
        month_siguiente = 1
        year_actual = year
        year_anterior = year
        year_siguiente = year+1
    } 

    
    var containerCards = document.getElementById("semanas");
    if ( containerCards.hasChildNodes() )
    {
        while ( containerCards.childNodes.length >= 1 )
        {
            containerCards.removeChild( containerCards.firstChild );
        }
    } 
    /* containerCards.classList.remove("semanas");
    containerCards.classList.add("semanas");  */
    let link_mes_anterior = "mes_anterior"+"("+ month_anterior + "," + year_anterior + ");";
    let link_mes_atual = "mes_actual"+"("+ month_actual + "," + year_actual + ");";
    let link_mes_siguiente = "mes_siguiente"+"("+ month_siguiente + "," + year_siguiente + ");";
    /* var semana6 = document.createElement('div');
    semana6.setAttribute("id", "semana6"); 
    semana6.classList.add("semana6");
    containerCards.appendChild(semana6); */
    
    document.getElementById("mes_anterior").setAttribute("onclick",link_mes_anterior);
    document.getElementById("mes_actual").setAttribute("onclick",link_mes_atual);
    document.getElementById("mes_siguiente").setAttribute("onclick",link_mes_siguiente);
    document.getElementById("mes_actual").textContent = meses[month_actual] + "  " + year_actual; 
    const mes_year = window.origin + "/mes_calendar/" + month_actual + "/" + year_actual + "/"
   
    fetch(mes_year)
    .then(res => res.json())
    .then(data =>{
       var casillas_llenas = 0
       var cont = 0
       var semana = 1
       var name_week = "semana" + semana
       var week = document.createElement('div');
       
       week.setAttribute("id", name_week); 
       week.classList.add("semana");
       containerCards.appendChild(week);
        
       for (const key in data) {
           cont += 1 
           casillas_llenas += 1
           if ( cont <= 7 ){
                name_id_day = "sem" + semana + "_" + "d" + cont
                name_id_service = "sem" + semana + "_" + "d" + cont + "s"
                let item_semana = document.createElement('div');
                item_semana.classList.add("numeroDia__semana");
                week.appendChild(item_semana);
                let name_day = document.createElement('div');
                name_day.setAttribute("id", name_id_day); 
                name_day.classList.add("day_month");
                let name_service = document.createElement('div');
                name_service.setAttribute("id", name_id_service); 
                name_service.classList.add("service");
                item_semana.appendChild(name_day);
                item_semana.appendChild(name_service);
                num_day = data[key]
                name_day.textContent =  num_day; 
           } 
           if ( cont == 7 ){
                semana += 1
                name_week = "semana" + semana
                week = document.createElement('div');
                week.setAttribute("id", name_week); 
                week.classList.add("semana");
                containerCards.appendChild(week);
                cont = 0
           }  
           if (data[key] != ""){
                console.log(key)
                let id_day_week = document.getElementById(key);
                let function_new_move = "new_move"+"("+ data[key] + "," + month_actual + "," +  year_actual+");";
                id_day_week.setAttribute("onclick",function_new_move);
           }
           if ( casillas_llenas > 21 &&  data[key] == '' ){
               primer_vacio.push(casillas_llenas)
               semana_vacio.push(semana)
           }  
        }
        let casilla_vacia = primer_vacio[0]
        let casilla_semana = semana_vacio[0]

        diferencia = (7 * casilla_semana) - casilla_vacia
        if (diferencia == 6 && casilla_semana==5){
         document.getElementById("semana5").remove()
         document.getElementById("semana6").remove()
         document.getElementById("semana7").remove()
        }
        
        if (diferencia < 6 && casilla_semana == 5){
          document.getElementById("semana6").remove()
          document.getElementById("semana7").remove()
        }
 
        if (diferencia == 6 && casilla_semana==6){
          document.getElementById("semana6").remove()   
          document.getElementById("semana7").remove()
        }

        if (diferencia == 7 && casilla_semana==6){
          document.getElementById("semana6").remove()   
          document.getElementById("semana7").remove()
        }
 
        if (diferencia < 6 && casilla_semana == 6){
         document.getElementById("semana7").remove()
        } 
    })

}




function mes_actual(month, year) {
    let month_actual = month;
    let year_actual = year;
    let meses = ["undefine", "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto",
                "Septiembre","Octubre", "Noviembre", "Diciembre"];
    document.getElementById("mes_actual").textContent = meses[month_actual] + " , " + year_actual; 
    const mes_year = window.origin + "/mes_calendar/" + month_actual + "/" + year_actual + "/"
    //console.log(mes_year)
    fetch(mes_year)
    .then(res => res.json())
    .then(data =>{
       for (const key in data) {
           if (data.hasOwnProperty(key)) {
               document.getElementById(key).textContent = data[key]  
               num_dias_semanas = num_dias_semanas + 1
               //console.log(num_dias_semanas, key)
               dias_vacios.push(num_dias_semanas)
               if(num_dias_semanas <= 35) {
                    document.getElementById(key).textContent = data[key]   
               }else{   
                document.getElementById("semana6").remove()
                semana6.setAttribute("id", "semana6"); 
                semana6.classList.add("semana6");
                containerCards.appendChild(semana6);
                num_day = data[key]
                id_dias_vacios.push(key)
                console.log(key)
                let listItem = document.createElement('div');
                listItem.setAttribute("id", key); 
                listItem.classList.add("numeroDia__semana");
                semana6.appendChild(listItem);
                listItem.textContent =  num_day; 

               }  
           }
       }

       id_dias_vacios.forEach(function (elemento, indice, array) {
        primer_day_semana6 = data["sem6_d1"]
        if (data[elemento]=="" && primer_day_semana6 == "") {
            document.getElementById(elemento).remove()  
        }
    });
       
    })
}

function mes_siguiente(month, year) {
    let month_actual = month;
    let year_actual = year;
    let month_anterior = month_actual - 1
    let year_anterior = year_actual 
    let month_siguiente = month_actual + 1
    let year_siguiente = year_actual 
    var dias_vacios = []
    var id_dias_vacios = []
    var primer_vacio = []
    var semana_vacio = []


    let meses = ["undefine", "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto",
                "Septiembre","Octubre", "Noviembre", "Diciembre"];
    if (month_anterior==0) {
        month_anterior = 12
        year_anterior = year-1
    }

    if (month_siguiente==13) {
        month_anterior = 11
        month_actual = 12
        month_siguiente = 1
        year_actual = year
        year_anterior = year
        year_siguiente = year+1 
    }


    var containerCards = document.getElementById("semanas");
    if ( containerCards.hasChildNodes() )
    {
        while ( containerCards.childNodes.length >= 1 )
        {
            containerCards.removeChild( containerCards.firstChild );
        }
    } 
    let link_mes_anterior = "mes_anterior"+"("+ month_anterior + "," + year_anterior + ");";
    let link_mes_atual = "mes_actual"+"("+ month_actual + "," + year_actual + ");";
    let link_mes_siguiente = "mes_siguiente"+"("+ month_siguiente + "," + year_siguiente + ");";
   
    document.getElementById("mes_anterior").setAttribute("onclick",link_mes_anterior);
    document.getElementById("mes_actual").setAttribute("onclick",link_mes_atual);
    document.getElementById("mes_siguiente").setAttribute("onclick",link_mes_siguiente);
    document.getElementById("mes_actual").textContent = meses[month_actual]  + "  " + year_actual; 
    /*document.getElementById("mes_anterior").textContent = month_anterior  + " , " + year_anterior;
    document.getElementById("mes_siguiente").textContent = month_siguiente  + " , " + year_siguiente;*/
    const mes_year = window.origin + "/mes_calendar/" + month_actual + "/" + year_actual + "/"
    //console.log(mes_year)
    fetch(mes_year)
    .then(res => res.json())
    .then(data =>{
        var casillas_llenas = 0
        var cont = 0
        var semana = 1
        var name_week = "semana" + semana
        var week = document.createElement('div');
        
        week.setAttribute("id", name_week); 
        week.classList.add("semana");
        containerCards.appendChild(week);
         
        for (const key in data) {
            cont += 1 
            casillas_llenas += 1
            if ( cont <= 7 ){
                 name_id_day = "sem" + semana + "_"  + "d" + cont
                 name_id_service = "sem" + semana + "_" + "d" + cont + "s"
                 let item_semana = document.createElement('div');
                 item_semana.classList.add("numeroDia__semana");
                 week.appendChild(item_semana);
                 let name_day = document.createElement('div');
                 name_day.setAttribute("id", name_id_day); 
                 name_day.classList.add("day_month");
                 let name_service = document.createElement('div');
                 name_service.setAttribute("id", name_id_service); 
                 name_service.classList.add("service");
                 item_semana.appendChild(name_day);
                 item_semana.appendChild(name_service);
                 num_day = data[key]
                 name_day.textContent =  num_day; 
            } 
            if ( cont == 7 ){
                 semana += 1
                 name_week = "semana" + semana
                 week = document.createElement('div');
                 week.setAttribute("id", name_week); 
                 week.classList.add("semana");
                 containerCards.appendChild(week);
                 cont = 0
            }  
            if (data[key] != ""){
                console.log(key)
                let id_day_week = document.getElementById(key);
                let function_new_move = "new_move"+"("+ data[key] + "," + month_actual + "," +  year_actual+");";
                id_day_week.setAttribute("onclick",function_new_move);
           }
            if ( casillas_llenas > 21 &&  data[key] == '' ){
                primer_vacio.push(casillas_llenas)
                semana_vacio.push(semana)
            }  
         }
         let casilla_vacia = primer_vacio[0]
         let casilla_semana = semana_vacio[0]
          
        diferencia = (7 * casilla_semana) - casilla_vacia
        if (diferencia == 6 && casilla_semana==5){
         document.getElementById("semana5").remove()
         document.getElementById("semana6").remove()
         document.getElementById("semana7").remove()
        }
        
        if (diferencia < 6 && casilla_semana == 5){
          document.getElementById("semana6").remove()
          document.getElementById("semana7").remove()
        }
 
        if (diferencia == 6 && casilla_semana==6){
         document.getElementById("semana6").remove()   
         document.getElementById("semana7").remove()
        }

        if (diferencia == 7 && casilla_semana==6){
            document.getElementById("semana6").remove()   
            document.getElementById("semana7").remove()
        }
 
        if (diferencia < 6 && casilla_semana == 6){
         document.getElementById("semana7").remove()
        } 

        console.log(diferencia)
    })
}