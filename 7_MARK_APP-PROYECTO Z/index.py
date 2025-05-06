from flask import Flask,render_template,redirect,url_for,jsonify,request
from db import inicializar_mysql
from config import configuracion

app= Flask(__name__)

mysql_conexion = inicializar_mysql(app)

@app.route('/')
def index():
    try:
        cur=mysql_conexion.connection.cursor()
        consulta_sql='SELECT * FROM tabla '
        cur.execute(consulta_sql)
        datos = cur.fetchall()
        print(datos)
        return render_template('principal.html',datos=datos)
    except Exception as ex:
        return "Error"
def no_encontrado(error):
    print("ESTE CODIGO SOLO SE MOSTRAR EN EL TERMINAR SU SE LLAMA A ESTA FUNCION")
    return "<h1>PAGINA NO ENCONTRADA .....</h1>"

@app.route('/agregar', methods=['POST'])
def agregar():
    if request.method =='POST':
        numero=request.form['numero']
        nombre=request.form['nombre']
        print(numero)
        print(nombre)
        cur=mysql_conexion.connection.cursor()
        consulta_sql = 'INSERT INTO tabla (numero, nombre) VALUES (%s, %s)'
        cur.execute(consulta_sql, (numero, nombre))
        mysql_conexion.connection.commit()
        return redirect(url_for('index'))

@app.route('/json')
def json():
    try:
        cur=mysql_conexion.connection.cursor()
        consulta_sql='SELECT * FROM tabla'
        cur.execute(consulta_sql)
        datos = cur.fetchall()
        print(datos)
        lista=[]
        for fila in datos:
            individual={'numero':fila[0],'nombre':fila[1]}
            lista.append(individual)
        return jsonify({'Enlistados':lista, 'mensaje':'ENCONTRADOS!'})
    except Exception as ex:
        return "Error"

@app.route('/json/<numero>')
def json_unidad(numero):
    try:
        cur=mysql_conexion.connection.cursor()
        consulta_sql="SELECT * FROM tabla WHERE numero = '{0}'".format(numero)
        cur.execute(consulta_sql)
        datos = cur.fetchone()
        if datos != None:
            individual={'numero':datos[0],'nombre':datos[1]}
            return jsonify({'Enlistado':individual, 'mensaje':'ENCONTRADO!'})
        else:
            return jsonify({'mensaje':'NO ENCONTRADO!'})
    except Exception as ex:
        return "Error"

@app.route('/eliminar/<numero>')
def eliminar(numero):
    cur=mysql_conexion.connection.cursor()
    consulta_sql="DELETE FROM tabla WHERE numero = %s"
    cur.execute(consulta_sql,(numero,))
    mysql_conexion.connection.commit()
    datos = cur.fetchall()
    print(datos)
    return redirect(url_for('index'))

@app.route('/editar/<numero>')
def editar(numero):
    cur = mysql_conexion.connection.cursor()
    consulta_sql = "SELECT * FROM tabla WHERE numero = %s"
    cur.execute(consulta_sql, (numero,))
    data = cur.fetchone()
    print(data)
    return render_template('editar.html', contact=data)

@app.route('/actualizar/<numero>',methods=['POST'])
def actualizar(numero):
    if request.method =='POST':
        nombre=request.form['nombre']
        cur=mysql_conexion.connection.cursor()
        consulta_sql = "UPDATE tabla SET nombre = %s WHERE numero = %s"
        cur.execute(consulta_sql, (nombre, numero))
        mysql_conexion.connection.commit()
        return redirect(url_for('index'))

if __name__=='__main__':
    app.config.from_object(configuracion)
    app.register_error_handler(404, no_encontrado)
    app.run(port=7000)
