function api(){
    var entry = {
        coordenadas: [
            "new google.maps.LatLng(4.443581, -75.231992)",
            "new google.maps.LatLng(4.443581, -75.231992)",
            "new google.maps.LatLng(4.443581, -75.231992)",
            "new google.maps.LatLng(4.443581, -75.231992)",
            "new google.maps.LatLng(4.443581, -75.231992)",
            "new google.maps.LatLng(4.443581, -75.231992)",
            "new google.maps.LatLng(4.443581, -75.231992)",
            "new google.maps.LatLng(4.443581, -75.231992)",
            "new google.maps.LatLng(4.443581, -75.231992)",
            "new google.maps.LatLng(4.443581, -75.231992)"
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
            let newarray = coodenadas_array.map(num_coordenada)
            function num_coordenada(item) {
                mis_item = "<li>" + item + "</li>"
                return mis_item;
              }
              coodenadas.innerHTML = ` ${newarray} <br> `
          });
        })
        .catch(function (error) {
          console.log("Fetch error: " + error);
        });
}

