var sobre_my = document.getElementById('sobre-my');
var titulo_items = document.getElementById('titulo-items');
var r = 0;
var g = 0;
var b = 0;

// Retorna un número aleatorio entre min (incluido) y max (excluido)
function getRandomArbitrary(min, max) {
    return Math.random() * (max - min) + min;
}

sobre_my.addEventListener('mouseout', function(e) {
    r = getRandomArbitrary(0, 256)
    g = getRandomArbitrary(0, 256)
    b = getRandomArbitrary(0, 256)
    color = "rgb("+ r + ","+ g + ","+ b +")"
    sobre_my.style.background = color;
    colort = "rgb("+ b + ","+ g + ","+ r +")"
    titulo_items.style.background = colort;
})