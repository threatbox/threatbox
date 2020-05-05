from wtforms import Form, BooleanField, StringField, PasswordField, \
    SelectField, RadioField, validators

# https://flask.palletsprojects.com/en/1.1.x/patterns/wtforms/


class RegistroForm(Form):
    username = StringField('Nombre de Usuario', [validators.DataRequired()]) 
    email = StringField('Email', [validators.Email(), validators.DataRequired()])
    password = PasswordField('Contraseña', [
        validators.DataRequired(),
        validators.EqualTo('password2', message='Las contraseñas no coinciden')
    ])
    password2 = PasswordField('Confirma Contraseña')


class LoginForm(Form):
    username = StringField('Nombre de Usuario') 
    password = PasswordField('Confirma')


# https://teamtreehouse.com/community/using-wtforms-for-selectfield-in-flask

             
class FuenteForm(Form):
    categoria = SelectField(
        'Categoría',
        choices=(
            (None, 'Selecciona...'),
            ('Terrorismo', 'Terrorismo'),
            ('Hacking', 'Hacking'),
            ('Cibercrimen', 'Cibercrimen'),
            ('Fraude', 'Fraude'),
            ('Ciberamenaza', 'Ciberamenaza'),
        )
    )
    subcategoria = SelectField(
        'Sub-Categoría',
        choices=(
            (None, 'Selecciona...'),
            ('Actor estatal', 'Actor estatal'),
            ('Armamento', 'Armamento'),
            ('Armamento improvisado', 'Armamento improvisado'),
            ('Botnet', 'Botnet'),
            ('Ciberguerra', 'Ciberguerra'),
            ('Criptojacking', 'Criptojacking'),
            ('Data Breach', 'Data Breach'),
            ('Data Leak', 'Data Leak'),
            ('Delincuencia organizada', 'Delincuencia organizada'),
            ('DDoS', 'DDoS'),
            ('Drogas', 'Drogas'),
            ('Extremismo de derechas', 'Extremismo de derechas'),
            ('Extremismo de izquierdas', 'Extremismo de izquierdas'),
            ('Hacktivismo', 'Hacktivismo'),
            ('Milicia', 'Milicia'),
            ('Phising', 'Phising'),
            ('Spam', 'Spam'),
            ('Yihad', 'Yihad'),
        )
    )
    fuente = StringField('Fuente', [validators.DataRequired()])
    ubicacion = SelectField(
        'Ubicación de la fuente',
        choices=(
            (None, 'Selecciona...'),
            ('Blog', 'Blog'),
            ('Buscador', 'Buscador'),
            ('Descargas', 'Descargas'),
            ('Directorio', 'Directorio'),
            ('Ecommerce', 'Ecommerce'),
            ('Foro', 'Foro'),
            ('Web personal', 'Web personal'),
            ('Wiki', 'Wiki'),
        )
    )
    direccion = StringField('Dirección web de la fuente', [validators.DataRequired()])
    darknet = RadioField(
        'Darknet',
        choices=(
            ('SI', 'SI'),
            ('NO', 'NO')
        )
    )
    tipo = SelectField(
        'Tipo de darknet',
        choices=(
            (None, 'Selecciona...'),
            ('darkAnt', 'ANts P2P'),
            ('darkEntro', 'Entropy'),
            ('darkFree', 'Freenet'),
            ('darkGnu', 'GNUnet'),
            ('darkMeta', 'Metanet'),
            ('darkI2p', 'i2p'),
            ('darkTor', 'Tor'),
            ('darkZero', 'Zeroet'),
        )
    )
    idioma = SelectField(
        'Idioma',
        choices=(
            (None, 'Selecciona...'),
            ('Alemán', 'Alemán'),
            ('Árabe', 'Árabe'),
            ('Chino', 'Chino'),
            ('Croata', 'Croata'),
            ('Español', 'Español'),
            ('Francés', 'Francés'),
            ('Griego', 'Griego'),
            ('Holandés', 'Holandés'),
            ('Indonesio', 'Indonesio'),
            ('Inglés', 'Inglés'),
            ('Italiano', 'Italiano'),
            ('Japonés', 'Japonés'),
            ('Polaco', 'Polaco'),
            ('Portugués', 'Portugués'),
            ('Ruso', 'Ruso'),
            ('Sueco', 'Sueco'),
            ('Turco', 'Turco'),
            ('Ucraniano', 'Ucraniano'),
        )
    )
    nivel = SelectField(
        'Nivel de actividad',
        choices=(
            (None, 'Selecciona...'),
            ('Alta', 'Alta'),
            ('Media', 'Media'),
            ('Baja', 'Baja'),
        )        
    )
    invitacion = RadioField(
        'Invitacion',
        choices=(
            ('SI', 'SI'),
            ('NO', 'NO')
        )
    )
    fiabilidad = RadioField(
        'Score de fiabilidad',
        choices=(
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
        )
    )