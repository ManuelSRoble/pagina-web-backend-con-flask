from flask import Flask, render_template, request, flash
#importo las funciones para crear un formulario
from formFunctions import *
from db import *
    
app = Flask(__name__)
app.config['SECRET_KEY'] = 'This is the most secure key to protect the forms'

@app.route('/', methods=['POST', 'GET'])
def registro():
  form = RegistroFormulario()
  if form.validate_on_submit():
    if request.method == 'POST':
      nombreDeUsuario = request.form['usuario']
      email = request.form['correo']
      clave = request.form['contrasena']
      # confirmacionDeClave = request.form['confirmar_contrasena']
      edad = request.form['edad']
      #if clave == confirmacionDeClave:
      agregar_usuario(nombreDeUsuario, email, clave, edad)
      return '<h1>Usuario agregado</h1>'
    
      '''
      datos = mostrar_usuarios()
      #renderizar la plantilla html y pasar los datos recuperados como contexto
      return render_template('tres_en_raya.html', data = datos) 
      '''
  # if form.validate_on_submit():
  #   return 'Formulario validado con exito'
  return render_template('formularioDeRegistro.html', form = form)

@app.route('/login')
def login():
  pass

@app.route('/admin')
def admin():
  #ver datos de la tabla usuario de bd
  datos = mostrar_usuarios()
  titulo = 'Ventana Admin'
  return render_template('admin.html', datos=datos, titulo = titulo)

if __name__ == '__main__':
  app.run(debug=True)