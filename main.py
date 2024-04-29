from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length, Email, EqualTo, NumberRange, ValidationError
from flask_wtf import CSRFProtect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'This is the most secure key to protect the forms'

def validar_usuario(form, field):
  if not field.data.isalpha():
    raise ValidationError('El usuario solo debe contener letras')
  
def validar_contrasena(form, field):
  if len(field.data) < 4:
    raise ValidationError('La contra debe contener 4 caracteres como minimo')

def validar_confirmar_contrasena(form, field):
  if field.data != form.contrasena.data:
    raise ValidationError('La contrasena no coincide')
  
def validar_edad(form, field):
  if not 18 <= field.data <=120:
    raise ValidationError('La edad esta fuera del rango del 18 al 120')
  
def validar_correo(form, field):
  #lista de dominios permitidos
  dominios_permitidos = ['gmail.com','hotmail.com']
  dominio = field.data.split('@')[-1]
  if dominio not in dominios_permitidos:
    raise ValidationError('El correo electronico debe tener un dominio permitido')
  
class RegistroFormulario(FlaskForm):
  usuario = StringField('Usuario', validators=[ DataRequired(), Length(min=4, max=25), validar_usuario])
  
  correo = StringField('Email', validators=[DataRequired(), Email(), validar_correo])
  contrasena = PasswordField('Password', validators=[DataRequired(), validar_contrasena])
  confirmar_contrasena = PasswordField('Confirmar password', validators=[DataRequired(), validar_confirmar_contrasena])
  edad = IntegerField('Edad/Age', validators=[DataRequired(), validar_edad])
  enviar = SubmitField('Enviar')
  
@app.route('/', methods=['POST', 'GET'])
def registro():
  form = RegistroFormulario()
  if form.validate_on_submit():
    #proceso los datos del formulario
    return 'Formulario validado con exito'
  return render_template('formularioDeRegistro.html', form = form)

if __name__ == '__main__':
  app.run(debug=True)