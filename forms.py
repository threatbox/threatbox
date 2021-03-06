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
            ('Ciberamenaza', 'Ciberamenaza'),
            ('Cibercrimen', 'Cibercrimen'),
            ('Fraude', 'Fraude'),
            ('Hacking', 'Hacking'),
            ('Terrorismo', 'Terrorismo'),
        )
    )
    subcategoria = SelectField(
        'Sub-Categoría',
        choices=(
            (None, 'Selecciona...'),
            ('0day', '0day'),
            ('Actor estatal', 'Actor estatal'),
            ('Armamento', 'Armamento'),
            ('Armamento improvisado', 'Armamento improvisado'),
            ('Ataque a equipos IoT', 'Ataque a equipos IoT'),
            ('Black Hack', 'Black Hack'),
            ('Botnet', 'Botnet'),
            ('Ciberguerra', 'Ciberguerra'),
            ('Criptodivisas', 'Criptodivisas'),
            ('Criptojacking', 'Criptojacking'),
            ('Data Breach', 'Data Breach'),
            ('Data Leak', 'Data Leak'),
            ('Delicuencia organizada', 'Delicuencia organizada'),
            ('DDoS', 'DDoS'),
            ('Drogas', 'Drogas'),
            ('Extremismo de derechas', 'Extremismo de derechas'),
            ('Extremismo de izquierdas', 'Extremismo de izquierdas'),
            ('Hacktivismo', 'Hacktivismo'),
            ('Insiders', 'Insiders'),
            ('Malware', 'Malware'),
            ('Phising', 'Phising'),
            ('Spam', 'Spam'),
            ('Tarjetas de crédito', 'Tarjetas de crédito'),
            ('Whaling', 'Whaling'),
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
            ('Email Service', 'Email Service'),
            ('Ecommerce', 'Ecommerce'),
            ('Foro', 'Foro'),
            ('Hosting', 'Hosting'),
            ('Noticias', 'Noticias'),
            ('Red Social', 'Red Social'),
            ('Telegram', 'Telegram'),
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
            ('ANts P2P', 'ANts P2P'),
            ('Entropy', 'Entropy'),
            ('Freenet', 'Freenet'),
            ('GNUnet', 'GNUnet'),
            ('Metanet', 'Metanet'),
            ('i2p', 'i2p'),
            ('Riffle', 'Riffle'),
            ('Tor', 'Tor'),
            ('Zeronet', 'Zeronet'),
        )
    )
    idioma = SelectField(
        'Idioma',
        choices=(
            (None, 'Selecciona...'),
            ('Alemán', 'Alemán'),
            ('Árabe', 'Árabe'),
            ('Chino', 'Chino'),
            ('Coreano', 'Coreano'),
            ('Croata', 'Croata'),
            ('Español', 'Español'),
            ('Eslovaco', 'Eslovaco'),
            ('Francés', 'Francés'),
            ('Griego', 'Griego'),
            ('Holandés', 'Holandés'),
            ('Indonesio', 'Indonesio'),
            ('Inglés', 'Inglés'),
            ('Italiano', 'Italiano'),
            ('Noruego', 'Noruego'),
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
            ('0', '0'),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('4', '4'),
            ('5', '5'),
        )
    )
