from flask import Flask, render_template, request, flash
#importo las funciones para crear un formulario
from formFunctions import *
from db import *
    
app = Flask(__name__)
app.config['SECRET_KEY'] = 'This is the most secure key to protect the forms'

@app.route('/', methods=['POST', 'GET'])
def registro():
  if request.method == 'POST':
    nombreDeUsuario = request.form['usuario']
    email = request.form['correo']
    clave = request.form['contrasena']
    edad = request.form['edad']
    
    '''
    datos = mostrar_usuarios()
    #renderizar la plantilla html y pasar los datos recuperados como contexto
    return render_template('tres_en_raya.html', data = datos) 
    '''
    
  form = RegistroFormulario()
  # if form.validate_on_submit():
  #   return 'Formulario validado con exito'
  return render_template('formularioDeRegistro.html', form = form)

@app.route('/login')
def login():
  pass

if __name__ == '__main__':
  app.run(debug=True)