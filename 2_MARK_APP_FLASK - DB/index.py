# Importamos el modulo MYSQL desde el paquete flask_mysqldb para manejar la conexión a MySQL
from flask_mysqldb import MySQL

# Importamos Flask y funciones necesarias: render_template para renderizar páginas HTML,
# request para manejar solicitudes HTTP, redirect para redirigir a rutas, 
# url_for para construir URLs, y flash para mostrar mensajes al usuario.
from flask import Flask, render_template, request, redirect, url_for, flash

# Creamos la instancia de la aplicación Flask
app = Flask(__name__)

# Configuración de los parámetros para conectarse a MySQL
app.config['MYSQL_HOST'] = 'localhost'  
app.config['MYSQL_USER'] = 'root' 
app.config['MYSQL_PASSWORD'] = '' 
app.config['MYSQL_DB'] = 'python'
mysql = MySQL(app)

# Configuramos una clave secreta para manejar sesiones y mensajes flash
app.secret_key = 'mysecretkey'

# Definimos la ruta principal de la aplicación
@app.route('/')
def principales():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM tablita2')
    data = cur.fetchall()
    print(data)
    return render_template('index.html', contacts=data)

# Ruta para agregar un nuevo contacto
@app.route('/add_contact', methods=['POST'])
def add_contact():
    # Verificamos si la solicitud HTTP es de tipo POST (envío de formulario)
    if request.method == 'POST':
        nombre = request.form['nombre']
        telefono = request.form['telefono']
        edad = request.form['edad'] 
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO tablita2 (nombre, telefono, edad) VALUES (%s, %s, %s)', (nombre, telefono, edad))
        mysql.connection.commit()
        flash('Contact added successfully')
        return redirect(url_for('principales'))

@app.route('/edit/<id>')
def get_contact(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM tablita2 WHERE id = %s', (id,))
    data = cur.fetchall()
    print(data[0])
    return render_template('edit_contact.html', contact=data[0])

@app.route('/update/<id>', methods=['POST'])
def update_contact(id):
    if request.method== 'POST':
        nombre = request.form['nombre']
        telefono = request.form['telefono']
        edad = request.form['edad'] 
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE tablita2
            SET nombre= %s,
                telefono= %s,
                edad= %s
            WHERE id=%s
        """,(nombre, telefono, edad, id))
        mysql.connection.commit()
        flash('Contacto actualizado correctamente')
        return redirect(url_for('principales'))

# Ruta para eliminar un contacto
@app.route('/delete/<string:id>')
def delete_contact(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM tablita2 WHERE id = %s', (id,))
    mysql.connection.commit()
    flash('Contact deleted')
    return redirect(url_for('principales'))



# Ruta para mostrar la página de servicios
@app.route('/servicio')
def servicios():
    return render_template('servicio.html')
# Ruta para mostrar la página de contacto
@app.route('/contacto')
def contactos():
    return render_template('contacto.html')

# Bloque principal que ejecuta la aplicación Flask
if __name__ == '__main__':
    app.run(debug=True, port=2000)
