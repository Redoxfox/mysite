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
          {lat:-1.0197222,	lng:-71.9383333},
          {lat:7,	lng:-75.5},
          {lat:7.0902778,	lng:-70.7616667},
          {lat:10.75,	lng:-75},
          {lat:9,	lng:-74.3333333},
          {lat:5.5,	lng:-72.5},
          {lat:5.25	,lng:-75.5},
          {lat:1,	lng:-74},
          {lat:5.5,	lng:-71.5},
          {lat:2.5,	lng:-76.8333333},
          {lat:9.3333333,	lng:-73.5},
          {lat:6,	lng:-77},
          {lat:5,	lng:-74.1666667},
          {lat:8.3333333,	lng:-75.6666667},
          {lat:2.5,	lng:-69},
          {lat:1.6894444,	lng:-72.8202778},
          {lat:2.5,	lng:-75.75},
          {lat:11.5,	lng:-72.5},
          {lat:10,	lng:-74.5},
          {lat:3.5,	lng:-73},
          {lat:1.5,	lng:-78},
          {lat:8,	lng:-73},
          {lat:0.5,	lng:-76},
          {lat:4.5,	lng:-75.6666667},
          {lat:5,	lng:-76},
          {lat:12.5847222,	lng:-81.7005556},
          {lat:7,	lng:-73.25},
          {lat:9,	lng:-75},
          {lat:3.75,	lng:-75.25},
          {lat:3.75,	lng:-76.5},
          {lat:0.25,	lng:-70.75},
          {lat:5,	lng:-69.5}
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

            function dibujar(lat, long){
              
              L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
                }).addTo(map);
  
                L.marker([lat, long]).addTo(map)
                .bindPopup('A pretty CSS3 popup.<br> Easily customizable.')
                .openPopup();
              
            }
            var map = L.map('map').setView([7, -75.5], 6);
            for (let index = 0; index < LatLng.length; index++) {
              const element = LatLng[index];
              /*let Extra = document.createElement('div');
              let id_Extra  = "Extra" + index
              Extra.setAttribute("id", id_Extra);
              Extra.textContent = "latitud:"+element[0]+"---"+"longitud:"+element[1]
              coodenadas.appendChild(Extra);*/
             
              dibujar(element[0], element[1])
              }
          });
        })
        .catch(function (error) {
          console.log("Fetch error: " + error);
        });
}



