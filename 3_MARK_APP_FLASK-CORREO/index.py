from flask import Flask, render_template, request
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

@app.route("/web/email", methods=["GET", "POST"])
def email():
    if request.method == "POST":
        try:
            asunto = request.form["asunto"]
            nombre=request.form["nombre"]
            correo = request.form["correo"]
            mensaje = request.form["mensaje"]
            
            # Configuración del servidor SMTP
            servidor = smtplib.SMTP("smtp.gmail.com", 587)
            servidor.starttls()
            servidor.login("garciajhair22@gmail.com", "dtbg zznt vdkk dqaa")  # Usa contraseña de aplicación segura

            # Crear el mensaje
            msg = MIMEMultipart()  # Utilizar MIMEMultipart para incluir asunto y cuerpo del correo
            msg["From"] = "garciajhair22@gmail.com"
            msg["To"] = correo
            msg["Subject"] = asunto  # Asignar el asunto correctamente

            #CONSTRUIR EL CUERO DEL MENSAJE
            cuerpo_mensaje=f"El correo es {correo} \nHola que tal, yo soy {nombre}!!!!\nMi asunto es: {asunto} \nEsta es mi situacion {mensaje}"
            # Adjuntar el mensaje
            msg.attach(MIMEText(cuerpo_mensaje, "plain"))

            # Enviar el correo
            servidor.sendmail("garciajhair22@gmail.com", correo, msg.as_string())
            servidor.quit()

            return "Mensaje enviado con éxito"

        except Exception as e:
            return f"Ocurrió un error al enviar el correo: {str(e)}"
    else:
        return render_template("principal.html")

# Bloque principal que ejecuta la aplicación Flask
if __name__ == '__main__':
    app.run(debug=True, port=3000)