from flask import Flask, render_template, request, jsonify
from forms import Registration  # Importa la clase desde forms.py
import smtplib
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
    mensaje = None
    print("Este es un mensaje desde fuera 1")
    form = Registration()
    print("Este es un mensaje desde fuera 2")
    
    data = request.get_json()  # Obtener los datos JSON del cuerpo de la solicitud
    if data:
        form.asunto.data = data.get('asunto', '')
        asunto_sencillo = form.asunto.data
        form.nombre.data = data.get('nombre', '')
        nombre_sencillo = form.nombre.data
        form.correo.data = data.get('correo', '')
        correo_sencillo = form.correo.data
        form.contrasena.data = data.get('contrasena', '')
        contrasena_sencilla = form.contrasena.data
        form.confirmar_contrasena.data = data.get('confirmar_contrasena', '')
        form.mensaje.data = data.get('mensaje', '')
        mensaje_sencillo = form.mensaje.data

    if form.validate_on_submit():
        print("Este es un mensaje desde dentro 1")
        # Imprimir los datos en la terminal
        print(f"Asunto_sencillo: {asunto_sencillo}")
        print(f"Nombre_sencillo: {nombre_sencillo}")
        print(f"Correo_sencillo: {correo_sencillo}")
        print(f"Contrasena_sencilla: {contrasena_sencilla}")
        print(f"Mensaje_sencillo: {mensaje_sencillo}")
        
        try:
            # Configuración del servidor SMTP
            servidor = smtplib.SMTP("smtp.gmail.com", 587)
            servidor.starttls()
            servidor.login("garciajhair22@gmail.com", "dtbg zznt vdkk dqaa")  # Usa contraseña de aplicación segura
            # Crear el mensaje
            msg = MIMEMultipart()
            msg["From"] = correo_sencillo  # El remitente es el correo proporcionado en el formulario
            msg["To"] = "garciajhair22@gmail.com"  # Tu correo será el destinatario
            msg["Subject"] = asunto_sencillo

            # Construir el cuerpo del mensaje
            cuerpo_mensaje = (f"El correo es {correo_sencillo} \n"
                              f"Hola que tal, yo soy {nombre_sencillo}!!!!\n"
                              f"Mi asunto es: {asunto_sencillo} \n"
                              f"Esta es mi situación: {mensaje_sencillo}")

            # Adjuntar el cuerpo del mensaje
            msg.attach(MIMEText(cuerpo_mensaje, "plain"))
            # Enviar el correo
            servidor.sendmail(correo_sencillo, "garciajhair22@gmail.com", msg.as_string())
            servidor.quit()
            print("Correo enviado correctamente.")
        except Exception as e:
            print("Error:", str(e))
            return jsonify(success=False, message="Ocurrió un error al enviar el correo.")

        return jsonify(success=True, message="Registro y envío exitoso!")
    else:
        # Recopilar los errores para devolverlos en formato JSON
        errors = form.errors
        print("Errores de validación:", errors)  # Imprimir los errores en la terminal
        return jsonify(success=False, errors=errors)

if __name__ == '__main__':
    app.run(debug=True, port=6500)