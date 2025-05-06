from flask import Flask, render_template, redirect, url_for, request, session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secreto_llaves_prometeo'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/11_alchemy_tareas'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Modelos de la base de datos
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    name = db.Column(db.String(100))
    surnames = db.Column(db.String(100))
    password = db.Column(db.String(100))

class Task(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), db.ForeignKey('users.email'))
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    date_task = db.Column(db.DateTime, default=datetime.utcnow)

with app.app_context():
    db.create_all()


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    user = User.query.filter_by(email=email, password=password).first()
    
    if user:
        session['email'] = email
        session['name'] = user.name
        session['surnames'] = user.surnames
        return redirect(url_for('principal'))
    else:
        return render_template('index.html', message="Las credenciales no son correctas")

@app.route('/principal')
def principal():
    return render_template('principal.html')

@app.route('/tareas')
def tareas():
    try:
        email = session['email']
        tasks = Task.query.filter_by(email=email).all()
        return render_template('tareas.html', tasks=tasks)
    except:
        return redirect(url_for('index'))

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

@app.route('/new-task', methods=['POST'])
def newTask():
    title = request.form['title']
    description = request.form['description']
    email = session['email']
    dateTask = datetime.now()
    
    if title and description and email:
        new_task = Task(email=email, title=title, description=description, date_task=dateTask)
        db.session.add(new_task)
        db.session.commit()
        
    return redirect(url_for('tareas'))

if __name__ == '__main__':
    app.run(debug=True, port=12000)
