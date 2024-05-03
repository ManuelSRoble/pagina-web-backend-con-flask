#formulario con campos y validadores
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length, Email, EqualTo, NumberRange, ValidationError
from flask_wtf import CSRFProtect

def validar_usuario(form, field):
  if not field.data.isalpha():
    raise ValidationError('El usuario solo debe contener letras')

def validar_confirmar_contrasena(form, field):
  if field.data != form.contrasena.data:
    raise ValidationError('La contrasena no coincide')
  
def validar_edad(form, field):
  if not 18 <= field.data <=120:
    return ValidationError('La edad esta fuera del rango del 18 al 120')
  
def validar_correo(form, field):
  #lista de dominios permitidos
  dominios_permitidos = ['gmail.com','hotmail.com']
  dominio = field.data.split('@')[-1]
  if dominio not in dominios_permitidos:
    raise ValidationError('El correo electronico debe tener un dominio permitido')

class RegistroFormulario(FlaskForm):
  usuario = StringField('Usuario', validators=[ DataRequired(), Length(min=4, max=25), validar_usuario])
  
  correo = StringField('Email', validators=[DataRequired(), Email(), validar_correo])
  
  contrasena = PasswordField('Password', validators=[DataRequired(), Length(min=4, max=10, message='Debe tener entre 4 y 10 caracteres')])
  
  confirmar_contrasena = PasswordField('Confirmar password', validators=[
    DataRequired(), 
    Length(min=4, max=10, message='Debe tener entre 4 y 10 caracteres'), 
    validar_confirmar_contrasena])
  
  edad = IntegerField('Edad/Age', validators=[DataRequired(), validar_edad])
  enviar = SubmitField('Enviar')