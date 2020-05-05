import os

import bcrypt
from bson.objectid import ObjectId
from pymongo import MongoClient
from flask import Flask, render_template, request, session, flash, redirect, \
    url_for

import forms


app = Flask(__name__)
app.secret_key = 'clave super secreta de encriptación de sesión'
app.config['SESSION_TYPE'] = 'filesystem'


client = MongoClient(os.environ.get('MONGODB'))
db = client.threatbox
db_usr = db.usuarios
db_fee = db.fuentes
feeds = db.threatbox['feeds']

SEARCH_LIMIT = 100  # número máximo de resultados en las búsquedas


@app.route('/')
@app.route('/buscar')
def buscar():
    datos = db_fee.find()
    # print(datos)
    busca = request.args.get('busca', '')
    if busca:
        datos = db_fee.find({
            "$or": [
                {'categoria': {'$regex': busca}},
                {'subcategoria': {'$regex': busca}},
                {'fuente': {'$regex': busca}},
                {'ubicacion': {'$regex': busca}},
                {'direccion': {'$regex': busca}},
                {'darknet': {'$regex': busca}},
                {'tipo': {'$regex': busca}},
                {'idioma': {'$regex': busca}},
                # {'nivel': {'$regex': busca}},
                # {'invitacion': {'$regex': busca}},
                # {'fiabilidad': {'$regex': busca}}
            ]
        })
        
    datos = list(datos)
    return render_template('buscar.html', datos=datos, busca=busca)


@app.route('/search', methods=['POST', 'GET'])
def search():
    busqueda = request.form['busca']
    resultado_busqueda = db.find(
        'fuente', search=busqueda, filter={'related':True}, limit=SEARCH_LIMIT
    )
    resultados = (res['obj'] for res in resultado_busqueda['results'])
    return render_template('search.html', results=resultados)



@app.route('/login', methods=['POST', 'GET'])
def login():
    form = forms.LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        login_user = db_usr.find_one({
            'name' : form.username.data
        })
        print(login_user)
        if login_user:
            if bcrypt.checkpw(form.password.data.encode('utf-8'), login_user['password']):
                return redirect(url_for('user_up'))
            else:
                form.password.errors.append('La contraseña no coincide')
        else:
            form.username.errors.append('El usuario no existe')

    return render_template('login.html', form=form)


@app.route('/register', methods=['POST', 'GET'])
def register():
    form = forms.RegistroForm(request.form)
    if request.method == 'POST' and form.validate():
        existing_user = db_usr.find_one({'name' : form.username.data})
        # print(existing_user)
        if existing_user is None:
            hashpass = bcrypt.hashpw(
                form.username.data.encode('utf-8'), bcrypt.gensalt()
            )
            db_usr.insert({
                'name' : form.username.data, 
                'password' : hashpass, 
                'email' : form.email.data
            })
            session['name'] = form.username.data
            return redirect(url_for('login'))
        else:
            form.username.errors.append('El usuario ya existe')

    return render_template('register.html', form=form)


@app.route('/user_up')
def user_up():
    return render_template('bienvenida.html')


@app.route('/upload', methods=['POST', 'GET'])
def upload():
    form = forms.FuenteForm(request.form)
    if request.method == 'POST' and form.validate():
        pk = db_fee.insert_one(form.data).inserted_id
        return redirect(url_for('ficha', id=pk))

    return render_template('upload.html', form=form)


# https://pymongo.readthedocs.io/en/stable/tutorial.html

@app.route('/detalle/<id>')
def ficha(id):
    fee = db_fee.find_one({'_id': ObjectId(id)})
    print(id)
    print(list(fee))
    return render_template('ficha.html', fee=fee)


@app.route('/error')
def error():
    return '<h1>oh oh Algo anda mal</h1>'


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)