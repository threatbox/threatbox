import os

from pymongo import MongoClient
from flask import Flask, render_template, request, session, flash

app = Flask(__name__)
app.secret_key = 'clave super secreta de encriptación de sesión'
app.config['SESSION_TYPE'] = 'filesystem'


# app.config['MONGO_DBNAME'] = 'mongologinexample'
# app.config['MONGO_URI'] = 'http://127.0.0.1:27017'

client = MongoClient(os.environ.get('MONGODB'))
db = client.pruebasdb
usr = db.usuarios
fee = db.feeds


@app.route('/')
@app.route('/index')
def index():
    datos = usr.find()
    busca = request.args.get('busca', '')
    if busca:
        datos = usr.find({'uname': {'$regex': busca}})
    return render_template('index.html', datos=datos, busca=busca)

@app.route('/acceso')
def acceso():
    return render_template('login.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        name = request.form.get('uname')
        password = request.form.get('passw')
        
        x = usr.find({'uname': name, 'passw': password}).count()
        if x > 0:
            session['uname'] = name
            return render_template('repositorio.html')  # ,username = session['uname'])
        else:
            flash('Usuario o contraseña incorrectos')
            return render_template('login.html')
    else:
        return render_template('login.html')

@app.route('/register')
def register():
    return render_template("register.html")

@app.route('/register_user', methods=['POST', 'GET'])
def register_user():
    if request.method == 'POST':
        name = request.form.get("uname")
        password = request.form.get("passw")
        email = request.form.get("email")
        if name == "" or password == "" or email == "":
            # flash("all fields are necessary")
            return render_template("register.html")
        else:
            t = usr.find({"uname": name}).count()
            if t > 0:
                # flash("user already exists")
                return render_template("register.html")
            else:
                pk = usr.insert_one(
                    {"uname": name, "passw": password, "email": email}
                )
                print(pk)
                if pk is not None:
                    return "user added"
                else:
                    return render_template("login.html")
    # return render_template('register.html')

@app.route('/upload')
def upload():
    return render_template('repositorio.html')

@app.route('/update', methods=['POST', 'GET'])
def update():
    if request.method == 'POST':
        categoria = request.form.get('categoria')
        subcategoria = request.form.get('subcategoria')
        fuente = request.form.get('fuente')
        ubicacion = request.form.get('ubaciacion')
        direccion = request.form.get('direccion')
        darknet = request.form.get('darknet')
        tipo = request.form.get('tipo')
        idioma = request.form.get('idioma')
        nivel = request.form.get('nivel')
        invitacion = request.form.get('invitacion')
        fiabilidad = request.form.get('fiabilidad')
        pk = fee.insert_one(
                {'categoria': categoria, 'subcategoria': subcategoria,'fuente': fuente, 'ubicacion': ubicacion, 'direccion': direccion, 'darknet': darknet, 'tipo': tipo, 'idioma': idioma, 'nivel': nivel, 'invitacion': invitacion, 'fiabilidad': fiabilidad}
            )
        if pk is not None:
            return render_template('fuentes.html')
        else:
            return render_template('error')

@app.route('/fuente')
def fuente():
    return render_template('fuentes.html')

@app.route('/error')
def error():
    return '<h1>oh oh Algo anda mal</h1>'

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)