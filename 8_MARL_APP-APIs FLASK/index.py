from flask import Flask,redirect,url_for,jsonify
from flask_mysqldb import MySQL
from config import configuracion

app= Flask(__name__)
conex= MySQL(app)

@app.route('/')
def retorno():
    return redirect(url_for('listar_cursos'))

@app.route('/cursos_listados')
def listar_cursos():
    try:
        cursation = conex.connection.cursor()
        sql_consulta = "SELECT codigo, nombre, creditos FROM curso "
        cursation.execute(sql_consulta)
        datos = cursation.fetchall()
        print(datos)
        cursos_generales=[]
        for fila in datos:
            curso_individual={'codigo':fila[0],'nombre':fila[1],'creditos':fila[2]}
            cursos_generales.append(curso_individual)
        return jsonify({'cursos enlistados':cursos_generales, 'mensaje':'cursos listado!'})
    except Exception as ex:
        return "Error"

def no_encontrado(error):
    print("ESTE CODIGO SOLO SE MOSTRAR EN EL TERMINAR SU SE LLAMA A ESTA FUNCION")
    return "<h1>PAGINA NO ENCONTRADA .....</h1>"

@app.route('/cursos_listados/<codigo>')
def leer_curso(codigo):
    try:
        cursation = conex.connection.cursor()
        sql_consulta = "SELECT codigo, nombre, creditos FROM curso WHERE codigo = '{0}'".format(codigo)
        cursation.execute(sql_consulta)
        datos = cursation.fetchone()
        if datos != None:
            curso_individual={'codigo':datos[0],'nombre':datos[1],'creditos':datos[2]}
            return jsonify({'curso enlistado':curso_individual, 'mensaje':'CURSO ENCONTRADO!'})
        else:
            return jsonify({'mensaje':'CURSO NO ENCONTRADO!'})
    except Exception as ex:
        return "Error"

if __name__=='__main__':
    app.config.from_object(configuracion['desarrollo'])
    app.register_error_handler(404, no_encontrado)
    app.run(port=8000)
