import os

import bcrypt
from bson.objectid import ObjectId
from pymongo import MongoClient
from flask import Flask, render_template, request, session, redirect, \
    url_for
from flask_paginate import Pagination, get_page_args

import forms


app = Flask(__name__)
app.secret_key = 'clave super secreta de encriptación de sesión'
app.config['SESSION_TYPE'] = 'filesystem'

client = MongoClient(os.environ.get('MONGODB'))
db = client.threatbox
db_usr = db.usuarios
db_fee = db.fuentes
feeds = db.threatbox['feeds']

SEARCH_LIMIT = 1000  # número máximo de resultados en las búsquedas


@app.route('/')
@app.route('/buscar')
def buscar():
    page, per_page, offset = get_page_args(
        page_parameter='page', per_page_parameter='per_page'
    )
    datos = db_fee.find()
    busca = request.args.get('busca', '')
    if busca:
        datos = db_fee.find({
            "$or": [
                {'categoria': {'$regex': busca, '$options': 'i'}},
                {'subcategoria': {'$regex': busca, '$options': 'i'}},
                {'fuente': {'$regex': busca, '$options': 'i'}},
                {'ubicacion': {'$regex': busca, '$options': 'i'}},
                {'direccion': {'$regex': busca, '$options': 'i'}},
                {'darknet': {'$regex': busca, '$options': 'i'}},
                {'tipo': {'$regex': busca, '$options': 'i'}},
                {'idioma': {'$regex': busca, '$options': 'i'}},
                # {'nivel': {'$regex': busca}},
                # {'invitacion': {'$regex': busca}},
                # {'fiabilidad': {'$regex': busca}}
            ]
        })
        # datos = list(datos)
        pagination = Pagination(page=page, total=datos.count(), busca=busca)
        datos = list(datos.skip(offset).limit(per_page))
    else:
        datos = []
        pagination = Pagination(page=page, total=0, busca=busca)

    return render_template(
        'buscar.html', datos=datos, busca=busca, pagination=pagination, total=len(datos)
    )


@app.route('/login', methods=['POST', 'GET'])
def login():
    form = forms.LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        login_user = db_usr.find_one({
            'name': form.username.data
        })
        if login_user:
            if bcrypt.checkpw(
                form.password.data.encode('utf-8'), login_user['password']
            ):
                session['name'] = form.username.data
                return redirect(url_for('upload'))
            else:
                form.password.errors.append('La contraseña no coincide')
        else:
            form.username.errors.append('El usuario no existe')

    return render_template('login.html', form=form)


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('buscar'))


@app.route('/register', methods=['POST', 'GET'])
def register():
    form = forms.RegistroForm(request.form)
    if request.method == 'POST' and form.validate():
        existing_user = db_usr.find_one({'name': form.username.data})
        if existing_user is None:
            hashpass = bcrypt.hashpw(
                form.password.data.encode('utf-8'), bcrypt.gensalt()
            )
            db_usr.insert({
                'name': form.username.data,
                'password': hashpass,
                'email': form.email.data
            })
            session['name'] = form.username.data
            return redirect(url_for('upload'))
        else:
            form.username.errors.append('El usuario ya existe')

    return render_template('register.html', form=form)


@app.route('/upload', methods=['POST', 'GET'])
def upload():
    if 'name' in session:
        form = forms.FuenteForm(request.form)
        if request.method == 'POST' and form.validate():
            pk = db_fee.insert_one(form.data).inserted_id
            return redirect(url_for('ficha', id=pk))

        return render_template('upload.html', form=form)
    else:
        return redirect(url_for('login'))


# https://pymongo.readthedocs.io/en/stable/tutorial.html

@app.route('/detalle/<id>')
def ficha(id):
    fee = db_fee.find_one({'_id': ObjectId(id)})
    return render_template('ficha.html', fee=fee)


@app.route('/error')
def error():
    return '<h1>oh oh Algo anda mal</h1>'


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
