function new_move(day, month, year){
    console.log(day, month, year);

}


function mes_anterior(month, year) {
    let month_actual = month;
    let year_actual = year;
    let month_anterior = month_actual - 1
    let year_anterior = year_actual 
    let month_siguiente = month_actual + 1
    let year_siguiente = year_actual 
    var dias_vacios = []
    var id_dias_vacios = []

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

  /*    if (month_anterior=11) {
        month_anterior = 11
        month_actual = 12
        month_siguiente = 1
        year_actual = year
        year_anterior = year
        year_siguiente = year
    } 
 */
    if (month_siguiente==13) {
        month_anterior = 11
        month_actual = 12
        month_siguiente = 1
        year_actual = year
        year_anterior = year
        year_siguiente = year+1
    } 

    
    let containerCards = document.getElementById("semanas");
    containerCards.classList.remove("semanas");
    containerCards.classList.add("semanas");
    let link_mes_anterior = "mes_anterior"+"("+ month_anterior + "," + year_anterior + ");";
    let link_mes_atual = "mes_actual"+"("+ month_actual + "," + year_actual + ");";
    let link_mes_siguiente = "mes_siguiente"+"("+ month_siguiente + "," + year_siguiente + ");";
    var semana6 = document.createElement('div');
    semana6.setAttribute("id", "semana6"); 
    semana6.classList.add("semana6");
    containerCards.appendChild(semana6);
    
    document.getElementById("mes_anterior").setAttribute("onclick",link_mes_anterior);
    document.getElementById("mes_actual").setAttribute("onclick",link_mes_atual);
    document.getElementById("mes_siguiente").setAttribute("onclick",link_mes_siguiente);
    document.getElementById("mes_actual").textContent = meses[month_actual] + "  " + year_actual; 
    /*document.getElementById("mes_anterior").textContent = month_anterior  + "  " + year_anterior;
    document.getElementById("mes_siguiente").textContent = month_siguiente  + " , " + year_siguiente;*/
    const mes_year = window.origin + "/mes_calendar/" + month_actual + "/" + year_actual + "/"
    //console.log(mes_year)
    fetch(mes_year)
    .then(res => res.json())
    .then(data =>{
       //console.log(data)
       num_dias_semanas = 0
       for (const key in data) {
           if (data.hasOwnProperty(key)) {
               //document.getElementById(key).textContent = data[key]  
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
                if (data[key] != ""){
                    let id_day_week = document.getElementById(key);
                    let function_new_move = "new_move"+"("+ data[key] + "," + month_actual + "," +  year_actual+");";
                    id_day_week.setAttribute("onclick",function_new_move);
                }
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


    let containerCards = document.getElementById("semanas");
    containerCards.classList.remove("semanas");
    containerCards.classList.add("semanas");
    let link_mes_anterior = "mes_anterior"+"("+ month_anterior + "," + year_anterior + ");";
    let link_mes_atual = "mes_actual"+"("+ month_actual + "," + year_actual + ");";
    let link_mes_siguiente = "mes_siguiente"+"("+ month_siguiente + "," + year_siguiente + ");";
    var semana6 = document.createElement('div');
    semana6.setAttribute("id", "semana6"); 
    semana6.classList.add("semana6");
    containerCards.appendChild(semana6);
    
    
    
    
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
       //console.log(data)
       num_dias_semanas = 0
       for (const key in data) {
           if (data.hasOwnProperty(key)) {
               num_dias_semanas = num_dias_semanas + 1
              //console.log(num_dias_semanas, key)
               dias_vacios.push(num_dias_semanas)
               
               if(num_dias_semanas <= 35) {
                    document.getElementById(key).textContent = data[key]  
                    let id_day_week = document.getElementById(key);
                    if (data[key] != ""){
                        let function_new_move = "new_move"+"("+ data[key] + "," + month_actual + "," +  year_actual+");";
                        id_day_week.setAttribute("onclick",function_new_move);
                    }
               }else{   
                    document.getElementById("semana6").remove()
                    semana6.setAttribute("id", "semana6"); 
                    semana6.classList.add("semana6");
                    containerCards.appendChild(semana6);
                    num_day = data[key]
                    id_dias_vacios.push(key)
                    let listItem = document.createElement('div');
                    listItem.setAttribute("id", key); 
                    listItem.classList.add("numeroDia__semana");
                    semana6.appendChild(listItem);
                    listItem.textContent =  num_day; 
                    if (data[key] != ""){
                        let id_day_week = document.getElementById(key);
                        let function_new_move = "new_move"+"("+ data[key] + "," + month_actual + "," +  year_actual+");";
                        id_day_week.setAttribute("onclick",function_new_move);
                    }
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