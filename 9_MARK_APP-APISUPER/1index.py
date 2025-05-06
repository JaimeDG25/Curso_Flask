from flask import Flask, jsonify, render_template,request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('1index.html')

@app.route('/pokemon/<int:pokemon_id>', methods=['GET'])
def get_pokemon(pokemon_id):
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_id}'
    response = requests.get(url)

    if response.status_code == 200:
        pokemon_data = response.json()
        print(f"ID: {pokemon_data['id']}, Nombre: {pokemon_data['name']}")
        return jsonify(response.json())
    
    return jsonify({"error": "Pokémon not found"}), 404

if __name__ == '__main__':
    app.run(debug=True ,port=9100)