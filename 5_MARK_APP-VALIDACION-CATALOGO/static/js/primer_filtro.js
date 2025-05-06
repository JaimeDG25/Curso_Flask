//alert("Comprobando que el primer filtro funciona")
const modal = document.getElementById('myModal_reserva'); // Cambia a 'registrationModal'
const modalSubmitButton = document.getElementById('modalSubmitButton');
const nombre1 = document.getElementById('nombre0');
const dni1 = document.getElementById('dni0');

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

// function capturarDatos() {
//     // Capturar el valor del destino
//     const destino = document.getElementById('destino_final').value;
//     // Capturar el precio final
//     const precioFinal = document.getElementById('precio_final').value;
//     // Capturar la cantidad de vuelos
//     const cantidadVuelos = document.getElementById('cantidad').value;
//     // Imprimir los valores en la consola
//     console.log('Destino capturarDatos():', destino);
//     console.log('Precio final capturarDatos():', precioFinal);
//     console.log('Cantidad de vuelos capturarDatos():', cantidadVuelos);
// }

modalSubmitButton.addEventListener('click', function () {

    const nombreValue = nombre1.value.trim();
    const dniValue = dni1.value.trim();
    let isValid = true;

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
    console.log('El nombre es: ',nombreValue)
    console.log('El dni es : ',dniValue)


    // Limpiar errores anteriores
    document.getElementById('nombreError').textContent = '';
    document.getElementById('dniError').textContent = '';

    // Validación de campos
    if (nombreValue === '') {
        isValid = false;
        document.getElementById('nombreError').textContent = 'El nombre es requerido.';
    }
    if (dniValue === '') {
        isValid = false;
        document.getElementById('dniError').textContent = 'El dni es requerido.';
    }
    if (isValid) {
        const csrfToken = document.querySelector('input[name="csrf_token"]').value;
        fetch('/submit_name', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                nombre8: nombreValue,
                dni8: dniValue,
                destino8: destino,
                precio_final8: precioFinal,
                cantidad8: cantidadVuelos,
                csrf_token: csrfToken
            })
        })
            .then(response => response.json())
            .then(result => {
                if (result.success) {
                    // Clear input fieldss
                    nombre1.value = '';
                    dni1.value = '';

                    // Close modal if submission is successful
                    const modalInstance = bootstrap.Modal.getInstance(modal);
                    modalInstance.hide();
                } else {
                    // Mostrar errores en el modal
                    if (result.errors) {
                        if (result.errors.nombre8) {
                            document.getElementById('nombreError').textContent = result.errors.nombre8;
                        }
                        if (result.errors.dni8) {
                            document.getElementById('dniError').textContent = result.errors.dni8;
                        }
                    }
                }
            })
            .catch(err => console.error('Error:', err));
    }
});