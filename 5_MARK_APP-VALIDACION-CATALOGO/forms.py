# forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, Regexp

class Registration(FlaskForm):

    nombre8 = StringField('Nombre', validators=[
        DataRequired(message='Este campo es obligatorio bro.'),
        Length(min=2, max=30, message='El nombre debe tener entre 2 y 30 caracteres bro.')
    ])
    dni8 = StringField('DNI', validators=[
    DataRequired(message='Este campo es obligatorio.'),
    Length(min=8, max=8, message='Ingrese la cantidad válida de DNI'),
    Regexp('^[0-9]*$', message='El DNI debe contener solo números.')  # Valida que solo se ingresen números
    ])
    submit = SubmitField('Registrar')