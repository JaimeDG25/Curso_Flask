# forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError
import re

class Registration(FlaskForm):
    asunto = StringField ('Asunto', validators=[
        DataRequired(message='Este campo es obligatorio.'),
        Length(min=2, max=40, message='El asunto debe tener entre 2 y 40 caracteres bro')
    ])
    nombre = StringField('Nombre', validators=[
        DataRequired(message='Este campo es obligatorio.'),
        Length(min=2, max=30, message='El nombre debe tener entre 2 y 30 caracteres bro.')
    ])
    correo = StringField('Correo', validators=[
        DataRequired(message='Este campo es obligatorio.'),
        Email(message='Por favor, ingresa un correo electrónico válido bro.')
    ])
    contrasena = PasswordField('Contraseña', validators=[
        DataRequired(message='Este campo es obligatorio.'),
        Length(min=6, max=35, message='La contraseña debe tener entre 6 y 35 caracteres bro.')
    ])
    confirmar_contrasena = PasswordField('Confirmar Contraseña',validators=[
        DataRequired(message='Este campo es obligatorio.'),
        EqualTo('contrasena', message='Las contraseñas no coinciden bro.')
    ])
    mensaje = TextAreaField('Descripción', validators=[
        DataRequired(message='Este campo es obligatorio.'),
        Length(min=10, max=500, message='La descripción debe tener entre 10 y 500 caracteres bro.')
    ])
    submit = SubmitField('Registrar')

    def validate_correo(self, correo):
        # Expresión regular para validar que el correo termine en .com
        if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.(com)$', correo.data):
            raise ValidationError('El correo debe ser válido y terminar en .com.')