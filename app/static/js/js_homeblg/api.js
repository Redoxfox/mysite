function api(){
    // Heatmap data
    function getPoints(LatLng) {
            
      const results = [];  
      for (let index = 0; index < LatLng.length; index++) {
        const element = LatLng[index];
        console.log(element[0],element[1])
        results.push("new google.maps.LatLng(" + element[0] +","+ element[1]+")");
      }
      return results; //Este array es la simulacion de lo que retorna la funcion original
     

      /*No pude tener acceso a la API por tal motivo la funcion new google.maps.LatLng(4.443581, -75.231992) no
      la reconoce mi codigo y me saca error pero trate de emular eso con un array que recibe los valores*/

        /*     return [
                new google.maps.LatLng(4.443581, -75.231992),
                new google.maps.LatLng(4.443884, -75.231993),
                new google.maps.LatLng(4.443887, -75.231994),
                new google.maps.LatLng(4.443890, -75.231995),
                new google.maps.LatLng(4.443893, -75.231996),
                new google.maps.LatLng(4.443896, -75.231997),
                new google.maps.LatLng(4.443604, -75.231996),
                new google.maps.LatLng(4.443750, -75.231998),
                new google.maps.LatLng(4.443740, -75.231685),
                new google.maps.LatLng(4.443738, -75.231680),
            ]; */
    }

    var entry = {
        coordenadas: [
            {lat:4.443581, lng:-75.230992},
            {lat:4.445581, lng:-75.231992},
            {lat:4.446581, lng:-75.232992},
            {lat:4.447581, lng:-75.233992},
            {lat:4.448581, lng:-75.234992},
            {lat:4.449581, lng:-75.235992},
            {lat:4.440581, lng:-75.236992},
            {lat:4.441581, lng:-75.237992},
            {lat:4.442581, lng:-75.238992},
            {lat:4.447581, lng:-75.239992}
        ]
      };
      url = window.origin + "/blog/ver_coordenadas/"
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
     
            console.log(data.array)
            let coodenadas = document.getElementById("coodenadas");
            coodenadas_array = data.array

            LatLng = coodenadas_array.map(num_coordenada)
              
            function num_coordenada (value){
              coord = []
              lat = value.lat
              lng = value.lng
              coord.push(lat)
              coord.push(lng)
              
              return coord;
            }
            
            console.log(getPoints(LatLng))//abre el inspector de elementos en el navegador cuando ejecutes y 
            //podras ver el array con los valores de las coordenadas.

            for (let index = 0; index < LatLng.length; index++) {
              const element = LatLng[index];
              let Extra = document.createElement('div');
              let id_Extra  = "Extra" + index
              Extra.setAttribute("id", id_Extra);
              Extra.textContent = "latitud:"+element[0]+"---"+"longitud:"+element[1]
              coodenadas.appendChild(Extra);
            }
            
           
          });
        })
        .catch(function (error) {
          console.log("Fetch error: " + error);
        });
}

