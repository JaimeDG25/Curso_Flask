from flask_mysqldb import MySQL

def inicializar_mysql(app):
    # Configurar los datos de conexión a MySQL
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = ''
    app.config['MYSQL_DB'] = 'data_base'
    
    # Inicializar la conexión con MySQL
    mysql_conexion = MySQL(app)
    
    return mysql_conexion
