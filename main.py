from flask import Flask, render_template, request, redirect, url_for, flash
#importo las funciones para crear un formulario
from formFunctions import *
from db import *
    
app = Flask(__name__)
app.config['SECRET_KEY'] = 'This is the most secure key to protect the forms'

@app.route('/', methods=['POST', 'GET'])
def registro():
  titulo = 'Tres en raya'
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
      return render_template('tresEnRaya.html', titulo=titulo)
    
      '''
      datos = mostrar_usuarios()
      #renderizar la plantilla html y pasar los datos recuperados como contexto
      return render_template('tres_en_raya.html', data = datos) 
      '''
  # if form.validate_on_submit():
  #   return 'Formulario validado con exito'
  return render_template('formularioDeRegistro.html', form = form)

@app.route('/login', methods=['POST','GET'])
def login():
  form = LoginForm()
  if form.validate_on_submit():
    email = request.form['correo']
    obtener = verificar_si_ya_esta_el_mail_en_la_bd(email)
    if obtener:
      #existe el mail en la bd
      #verificar si la clave es correcta
      contrasena = request.form['contrasena']
      contrasena = int(contrasena)
      clave_devuelta = verifico_clave_del_mail(email)
      c = clave_devuelta['clave']
      c = int(c)
      if c == contrasena:        
        return render_template('tresEnRaya.html')
      else:
        flash('Clave incorrecta')
    else:
      #el registro(el mail) no existe en la bd
      flash('Ese mail no esta registrado')
    
  return render_template('login.html', form=form)
  '''
    if request.method == 'POST':
      #obtener datos de la solicitud POST
      email = request.form['correo']
      esta = verificar_si_ya_esta_el_mail_en_la_bd(email)
      if esta: # el correo existe en la bd
        #obtengo la clave del formulario
        clave = request.form['contrasena']
        #verifico si la clave esta es la misma que la que esta guarda para ese mail
        
        return render_template('tresEnRaya.html', titulo='Tres en raya xo')
  '''

#ruta ppal para mostrar todos los registros
@app.route('/admin')
def admin():
  data = mostrar_usuarios()
  titulo = 'Ventana admin'
  return render_template('admin.html', datos=data, titulo=titulo)
  #ver datos de la tabla usuario de bd
  '''datos = mostrar_usuarios()
  eliminar = eliminar_usuario()
  titulo = 'Ventana Admin'
  return render_template('admin.html', datos=datos, titulo = titulo, eliminar=eliminar)'''

#ruta para modificar un usuario existente
@app.route('/actualizar/<int:id>', methods=['POST'])
def actualizar(id):
  name = request.form['name']
  #actualizar el registro en la bd
  actualizar_usuario(name, id)
  return redirect(url_for('admin'))

@app.route('/eliminar/<int:id>')
def eliminar(id):
  eliminar_usuario(id)
  return redirect(url_for('admin'))

if __name__ == '__main__':
  app.run(debug=True)