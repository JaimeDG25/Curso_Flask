document.getElementById('fetchPokemon').addEventListener('click', function() {
    const pokemonId = document.getElementById('pokemonId').value;

    if (!pokemonId) {
        alert('Por favor, ingresa un ID de Pokémon.');
        return;
    }

    fetch(`/pokemon/${pokemonId}`)
        .then(response => {
            if (!response.ok) {
                throw new Error('Pokémon no encontrado');
            }
            return response.json();
        })
        .then(data => {
            const pokemonInfoDiv = document.getElementById('pokemonInfo');
            pokemonInfoDiv.innerHTML = `
                <h2>${data.name}</h2>
                <p>Altura: ${data.height}</p>
                <p>Peso: ${data.weight}</p>
                <p>Tipos: ${data.types.map(type => type.type.name).join(', ')}</p>
                <img src="${data.sprites.front_default}" alt="${data.name}">
            `;
        })
        .catch(error => {
            const pokemonInfoDiv = document.getElementById('pokemonInfo');
            pokemonInfoDiv.innerHTML = `<p class="text-danger">${error.message}</p>`;
        });
});
