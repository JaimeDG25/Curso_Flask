let precioOriginal = 0;  // Variable global para almacenar el precio original

// Función que se llama al hacer clic en el botón de la tarjeta
function showName(buttonElement) {
    // Encuentra el destino y el precio en la tarjeta
    const destino = buttonElement.parentElement.querySelector('.destino').innerText;
    const precio = parseInt(buttonElement.parentElement.querySelector('.precio').innerText);
    
    // Asigna los valores a los inputs correspondientes
    document.getElementById('destino_final').value = destino;
    document.getElementById('precio_final').value = precio;
    
    // Almacena el precio original en la variable global
    precioOriginal = precio;
    
    // Mostrar en consola para verificar
    console.log('Destino showName():', destino);
    console.log('Precio original showName():', precio);
}

// Función para incrementar la cantidad y recalcular el precio
function increment() {
    var cantidadInput = document.getElementById('cantidad');
    var cantidad = parseInt(cantidadInput.value);
    
    // Incrementar la cantidad
    cantidadInput.value = cantidad + 1;
    
    // Calcular el nuevo precio total en relación a la cantidad
    const precioTotal = precioOriginal * (cantidad + 1);
    
    // Actualizar el precio final en el input de precio
    document.getElementById('precio_final').value = precioTotal;
    
    // Mostrar en consola para verificar
    console.log('Cantidad:', cantidadInput.value);
    console.log('Precio total:', precioTotal);
}

// Función para decrementar la cantidad y recalcular el precio
function decrement() {
    var cantidadInput = document.getElementById('cantidad');
    var cantidad = parseInt(cantidadInput.value);
    
    // Evitar que la cantidad sea menor que 1
    if (cantidad > 1) {
        cantidadInput.value = cantidad - 1;
        
        // Calcular el nuevo precio total en relación a la cantidad
        const precioTotal = precioOriginal * (cantidad - 1);
        
        // Actualizar el precio final en el input de precio
        document.getElementById('precio_final').value = precioTotal;
        
        // Mostrar en consola para verificar
        console.log('Cantidad:', cantidadInput.value);
        console.log('Precio total:', precioTotal);
    }
}

function capturarDatos() {
    // Capturar el valor del destino
    const destino = document.getElementById('destino_final').value;
    // Capturar el precio final
    const precioFinal = document.getElementById('precio_final').value;
    // Capturar la cantidad de vuelos
    const cantidadVuelos = document.getElementById('cantidad').value;
    // Imprimir los valores en la consola
    console.log('Destino capturarDatos():', destino);
    console.log('Precio final capturarDatos():', precioFinal);
    console.log('Cantidad de vuelos capturarDatos():', cantidadVuelos);
}

// // Función para enviar los datos (solo muestra en consola)
// function enviar() {
//     const destino = document.getElementById('destino_final').value;
//     const precio = document.getElementById('precio_final').value;
//     const cantidad = document.getElementById('cantidad').value;
//     const nombre= nombre.getElementById('nombre').value;
//     const dni=document.getElementById('dni').value;
    
//     console.log('Destino enviar():', destino);
//     console.log('Nombre enviar():',nombre);
//     console.log('Precio final enviar():', precio);
//     console.log('DNI enviar(); ',dni);
//     console.log('Cantidad enviar():', cantidad);
// }