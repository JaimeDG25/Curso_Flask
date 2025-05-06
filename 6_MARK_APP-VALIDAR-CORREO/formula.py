from flask import Flask, render_template, request
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def inicio():
    mensaje = None  # Inicializa la variable mensaje
    if request.method == "POST":
        try:
            asunto = request.form["asunto"]
            nombre = request.form["nombre"]
            correo_remitente = request.form["correo"]
            mensaje_input = request.form.get("mensaje", "")
            
            # Imprimir los datos en la consola
            print(asunto)
            print(nombre)
            print(correo_remitente)
            print(mensaje_input)
            
            # Configuración del servidor SMTP
            servidor = smtplib.SMTP("smtp.gmail.com", 587)
            servidor.starttls()
            servidor.login("garciajhair22@gmail.com", "dtbg zznt vdkk dqaa")  # Usa contraseña de aplicación segura

            # Crear el mensaje
            msg = MIMEMultipart()
            msg["From"] = correo_remitente  # El remitente es el correo proporcionado en el formulario
            msg["To"] = "garciajhair22@gmail.com"  # Tu correo será el destinatario
            msg["Subject"] = asunto

            # Construir el cuerpo del mensaje
            cuerpo_mensaje = f"El correo es {correo_remitente} \nHola que tal, yo soy {nombre}!!!!\nMi asunto es: {asunto} \nEsta es mi situacion {mensaje}"
            
            # Adjuntar el cuerpo del mensaje
            msg.attach(MIMEText(cuerpo_mensaje, "plain"))

            # Enviar el correo
            servidor.sendmail(correo_remitente, "garciajhair22@gmail.com", msg.as_string())
            servidor.quit()
            
            # Mensaje de éxito
            mensaje = "Formulario enviado correctamente."
            return render_template("formula.html", mensaje=mensaje)
        except Exception as e:
            print("Error:", str(e))
            return "Ocurrió un error al procesar el formulario."
    else:
        return render_template("formula.html")

if __name__ == '__main__':
    app.run(debug=True, port=10000)