from flask import Flask,render_template,request,jsonify
import requests
app= Flask(__name__)

@app.route('/')
def index():
    return render_template('2index.html')

@app.route('/envio', methods=['POST'])
def datos():
    data = request.get_json()
    entrenador = data.get('entrenador_json')
    numero = data.get('numero_json')
    print(f"Nombre: {entrenador}, Número: {numero}")
    return jsonify({
        'success': True,
        'mensaje': f'Recibido: Nombre: {entrenador}, Número: {numero}'
    })

# Nueva ruta para interactuar con la API externa
@app.route('/pokemon/<int:id>', methods=['GET'])
def obtener_pokemon(id):
    # Llamamos a la PokeAPI
    poke_api_url = f"https://pokeapi.co/api/v2/pokemon/{id}"
    response = requests.get(poke_api_url)
    
    if response.status_code == 200:
        pokemon_data = response.json()
        return jsonify({
            'success': True,
            'nombre': pokemon_data['name'],
            'id': pokemon_data['id'],
            'tipo': pokemon_data['types'][0]['type']['name']
        })
    else:
        return jsonify({
            'success': False,
            'mensaje': 'Pokémon no encontrado'
        }), 404

if __name__ == '__main__':
    app.run(debug=True, port=9200)