
        function getXmlHttpRequestObject() {
            if (window.XMLHttpRequest) {
                return new XMLHttpRequest();
            } else if(window.ActiveXObject) {
                return new ActiveXObject("Microsoft.XMLHTTP");
            } else {
                alert("Tu navegador no soporta la tecnología Ajax!Usa Firefox por ejemplo");
            }
        }
        var gestorPeticiones = getXmlHttpRequestObject();
        
        
        function obtenerSubCategorias() {
            if (gestorPeticiones.readyState == 4 || gestorPeticiones.readyState == 0) {
        
                var idliga  = document.formulario.id_liga.value;
                gestorPeticiones.open("POST", '/select', true);		
                gestorPeticiones.onreadystatechange = controlGetSubCategorias;
                gestorPeticiones.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
                gestorPeticiones.send("idCategoria="+idliga);
            }		
        }
        
        function cuotas() {
            if (gestorPeticiones.readyState == 4 || gestorPeticiones.readyState == 0) {
                gestorPeticiones.open("POST", '/MostrarCuotas', true);		
                gestorPeticiones.onreadystatechange = mostrar_valores;
                gestorPeticiones.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
            }	
         else {
            alert("Tu navegador no soporta la tecnología Ajax!Usa Firefox por ejemplo");
        }	
        }

        function mostrar_valores() {
            if (gestorPeticiones.readyState == 4) {
               let s = document.getElementById('valo_r');
               //console.log(gestorPeticiones.responseText);
               let Se = gestorPeticiones.responseText;

               alert(gestorPeticiones.responseText)
               // if (str === "1") {
                 //var str2 = "<select>"+"<option value='1'>a</option>"+"<option value='2'>b</option>"+"<option value='3'>c</option>"+"</select>";
               // }
               //console.log(str);
               //ss.innerHTML = str.FE;
               /*let cadlab = "<label for='pais'>Nombre Equipo:</label>";  
               let cadini = "<select name = 'subCategorias' id='eq_1'>";
               let cadmed = ""; 
               for (var i in str) {
                  cadmed += "<option value="+str[i].id+">"+str[i].nombre+"</option>";      
               }
               let cadfin = "</select>";
               //console.log(str2);
               ss.innerHTML = cadlab + cadini + cadmed + cadfin;

               let cadlab2 = "<label for='pais'>Nombre Equipo:</label>";  
               let cadini2 = "<select name = 'subCategorias2' id='eq_2'>";
               let cadmed2 = ""; 
               for (var i in str) {
                  cadmed2 += "<option value="+str[i].id+">"+str[i].nombre+"</option>";      
               }
               let cadfin2 = "</select>";
               //console.log(str2);
               ss2.innerHTML = cadlab2 + cadini2 + cadmed2 + cadfin2;*/
            }
            
        }
        
        
        function controlGetSubCategorias() {
            if (gestorPeticiones.readyState == 4) {
                var ss = document.getElementById('capaSubCategorias');
                var ss2 = document.getElementById('capaSubCategorias2');
               var str = JSON.parse(gestorPeticiones.responseText);
               // if (str === "1") {
                 //var str2 = "<select>"+"<option value='1'>a</option>"+"<option value='2'>b</option>"+"<option value='3'>c</option>"+"</select>";
               // }
               // ss.innerHTML = str2;
               let cadlab = "<label for='pais'>Nombre Equipo:</label>";  
               let cadini = "<select name = 'subCategorias' id='eq_1'>";
               let cadmed = ""; 
               for (var i in str) {
                  cadmed += "<option value="+str[i].id+">"+str[i].nombre+"</option>";      
               }
               let cadfin = "</select>";
               //console.log(str2);
               ss.innerHTML = cadlab + cadini + cadmed + cadfin;

               let cadlab2 = "<label for='pais'>Nombre Equipo:</label>";  
               let cadini2 = "<select name = 'subCategorias2' id='eq_2'>";
               let cadmed2 = ""; 
               for (var i in str) {
                  cadmed2 += "<option value="+str[i].id+">"+str[i].nombre+"</option>";      
               }
               let cadfin2 = "</select>";
               //console.log(str2);
               ss2.innerHTML = cadlab2 + cadini2 + cadmed2 + cadfin2;
            }
        }
   
