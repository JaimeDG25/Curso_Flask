from flask import Flask,request,jsonify,render_template,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/flaskmysql'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(70), unique=True)
    description = db.Column(db.String(100))

    def __init__(self, title, description):
        self.title = title
        self.description = description

with app.app_context():
    db.create_all()


class TaskSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'description')
    
task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)

@app.route('/tasks', methods=['Post'])
def create_task():
    title = request.json['title']
    description = request.json['description']
    new_task= Task(title, description)

    db.session.add(new_task)
    db.session.commit()

    return task_schema.jsonify(new_task)

@app.route('/tasks', methods=['GET'])
def get_tasks():
    all_tasks = Task.query.all()
    result = tasks_schema.dump(all_tasks)
    return jsonify(result) 

@app.route('/tasks/<id>', methods=['GET'])
def get_task(id):
    task = Task.query.get(id)
    return task_schema.jsonify(task)

@app.route('/tasks/<id>', methods=['PUT'])
def update_task(id):
    task = Task.query.get(id)

    title = request.json['title']
    description = request.json['description']

    task.title = title
    task.description = description

    db.session.commit()

    return task_schema.jsonify(task)

@app.route('/tasks/<id>', methods=['DELETE'])
def delete_task(id):
    task = Task.query.get(id)
    db.session.delete(task)
    db.session.commit()
    return task_schema.jsonify(task)

# @app.route('/', methods=['GET'])
# def index():
#     return jsonify({'message': 'Welcome to my API'})

@app.route('/', methods=['GET','POST'])
def inicio():
    return render_template('index.html')

@app.route('/añadir', methods=['POST'])
def añadir():
    titulo = request.form['title']
    descripcion = request.form['description']
    print(titulo)
    print(descripcion)
    new_task= Task(titulo, descripcion)

    db.session.add(new_task)
    db.session.commit()
    return redirect(url_for('inicio'))

@app.route('/mostrar', methods=['GET'])
def mostrar():
    all_tasks = Task.query.all()  # Obtiene todas las tareas
    return render_template('index.html', tasks=all_tasks)

@app.route('/eliminar/<int:id>', methods=['GET'])
def eliminar(id):
    task = Task.query.get(id)  # Encuentra la tarea por ID
    if task:
        db.session.delete(task)
        db.session.commit()
    return redirect(url_for('mostrar')) 


if __name__ =="__main__":
    app.run(debug=True, port=8000)