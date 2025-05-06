from flask import Flask,render_template,jsonify
from data import db_datos
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("4index.html")

@app.route("/dbz", methods=['GET'])
def obtener_todos():
    return jsonify(db_datos)

@app.route("/dbz/<int:dbz_id>", methods=['GET'])
def obtener(dbz_id):
    z_kai=db_datos.get(dbz_id)
    if z_kai:
        return jsonify(z_kai)
    else:
        return jsonify({"error": "Guerrero z no encontrado"}), 404
if __name__ == '__main__':
    app.run(debug=True, port=9400)
