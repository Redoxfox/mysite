
function dia_mes() {
      url = 'https://jsonplaceholder.typicode.com/users'
      fetch(url)
      .then(res => res.json())
      .then(data =>{
          console.log(data)
          /* for (let index = 0; index < data.length; index++) {
              const element = data[index];
              console.log(element)
              
          } */
          url2 =window.origin + '/Clientes/Users/'
          fetch(url2, {
            method: 'POST', // or 'PUT'
            credentials: "include",
            body: JSON.stringify(data), // data can be `string` or {object}!
            cache:"no-cache",
            headers: new Headers({
              'Content-Type': 'application/json'
            })
          }).then(res => res.json())
          .catch(error => console.error('Error:', error))
          .then(response => console.log('Success:', response));
      })   
}
  //window.onload=dia_mes;
  