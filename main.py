from flask import Flask, render_template, request
#importo las funciones para crear un formulario
from formFunctions import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'This is the most secure key to protect the forms'


  
@app.route('/', methods=['POST', 'GET'])
def registro():
  form = RegistroFormulario()
  if form.validate_on_submit():
    #proceso los datos del formulario
    return 'Formulario validado con exito'
  return render_template('formularioDeRegistro.html', form = form)

if __name__ == '__main__':
  app.run(debug=True)