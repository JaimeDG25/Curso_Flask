from flask import Flask, jsonify, render_template

app = Flask(__name__)

# Datos simulados de Pokémon
POKEMON_DATA = {
    1: {"name": "Bulbasaur", "type": ["grass", "poison"], "id": 1},
    2: {"name": "Ivysaur", "type": ["grass", "poison"], "id": 2},
    3: {"name": "Venusaur", "type": ["grass", "poison"], "id": 3},
    4: {"name": "Charmander", "type": ["dragon", "fire"], "id": 4}
}

# Ruta GET para servir el HTML
@app.route('/')
def index():
    return render_template('3index.html')

# Ruta para obtener detalles de un Pokémon por ID (GET)
@app.route('/pokemons/<int:pokemon_id>', methods=['GET'])
def get_pokemon(pokemon_id):
    pokemon = POKEMON_DATA.get(pokemon_id)
    if pokemon:
        return jsonify(pokemon)
    else:
        return jsonify({"error": "Pokemon not found"}), 404

if __name__ == '__main__':
    app.run(debug=True, port=9300)
