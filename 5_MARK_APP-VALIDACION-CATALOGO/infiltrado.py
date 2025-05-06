from flask import Flask, render_template, request, jsonify,url_for
from forms import Registration  # Importa la clase desde forms.py
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta'

@app.route("/", methods=["GET", "POST"])
def index():
    form = Registration()
    return render_template("infiltrado.html", form=form)

@app.route('/submit_name', methods=['POST'])
def submit_name():
    form = Registration()
    print("Este es un mensaje desde fuera 2")
    
    data = request.get_json()  # Obtener los datos JSON del cuerpo de la solicitud
    if data:
        form.nombre8.data = data.get('nombre8', '')
        nombre_sencillo = form.nombre8.data
        form.dni8.data = data.get('dni8', '')
        dni_sencillo = form.dni8.data
        print("Hola como andan")
        # Obtener los datos adicionales (destino, precio final, cantidad de vuelos)
        destino = data.get('destino8', '')
        precio_final = data.get('precio_final8', '')
        cantidad = data.get('cantidad8', '')

    if form.validate_on_submit():
        print("Este es un mensaje desde dentro 1")
        # Imprimir los datos en la terminal
        print("Datos recibidos:")
        print(f"Destino: {destino}")
        print(f"Precio final: {precio_final}")
        print(f"Cantidad de vuelos: {cantidad}")
        print(f"Nombre: {nombre_sencillo}")
        print(f"DNI: {dni_sencillo}")
        return jsonify(success=True, message="Registro y envío exitoso!")
    else:
        # Recopilar los errores para devolverlos en formato JSON
        errors = form.errors
        print("Errores de validación:", errors)  # Imprimir los errores en la terminal
        return jsonify(success=False, errors=errors)

if __name__ == '__main__':
    app.run(debug=True, port=5000)