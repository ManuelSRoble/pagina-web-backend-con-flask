import pymysql
import pymysql.cursors
#conexion a la bd
def conexionbd():
  try:
    db = pymysql.connect(
      host='localhost',
      user='root',
      passwd='',
      database='tres_en_raya',
      cursorclass=pymysql.cursors.DictCursor
    ) # uso cursor que devuelva un diccionario para trabajarlo mejor que con tuplas que es como devuelve por defecto 
    return db
  except pymysql.Error as e:
    print('Error al conectar a la bd', e)
    return None
  
def mostrar_usuarios():
  conexion = conexionbd()
  if conexion:
    #creo un cursor para ejecutar consultas sql
    cursor = conexion.cursor()
    # ejecutar la consulta sql, para insertar datos
    cursor.execute("SELECT * FROM usuarios_web")
    
    #obtener los datos de la consulta
    data = cursor.fetchall()
  
    #cerrar el cursor
    conexion.close()
    return data
    
def agregar_usuario(nombre, email, clave, edad):
  conexion = conexionbd()
  if conexion:
    #cursor para ejecutar consultas sql, insertar nuevo usuario a la bd
    cursor = conexion.cursor()
    
    #Insercion de datos a la tabla de 'usuarios_web'
    cursor.execute("INSERT INTO usuarios_web (nombre, email, clave, edad) VALUES (%s, %s, %s, %s)", (nombre, email, clave, edad))
    
    #guardar los datos en la bd
    conexion.commit()
    conexion.close() #cerrar conexion a la bd
    
#eliminar usuario de la bd
def eliminar_usuario(id):
  conexion = conexionbd()
  if conexion:
    #crear un cursor para ejecutar consultas sql
    cursor = conexion.cursor()
    
    # Instruccion sql para eliminar el usuario
    cursor.execute('DELETE FROM usuarios_web WHERE id = %s', (id,))
    # Ejecutar la instruccion sql con el identificador del usuario
    # cursor.execute(sql, (id_usuario,))
    
    #hacer commit para guardar los cambios
    conexion.commit()
    
    #cerrar el cursor y la conexion
    cursor.close()
    conexion.close()
    
def actualizar_usuario(nombre, id):
  conexion = conexionbd()
  if conexion:
    cursor = conexion.cursor()
    #actualizar el registro en la bd
    cursor.execute('UPDATE usuarios_web SET nombre = %s WHERE id = %s', (nombre, id))
    conexion.commit()
    conexion.close()
    
def verificar_si_ya_esta_el_mail_en_la_bd(email):
  conexion = conexionbd()
  if conexion:
    try:
      #crear un cursor para ejecutar consultas sql
      cursor = conexion.cursor()
      
      cursor.execute("SELECT email FROM usuarios_web WHERE email = %s", (email,))
      
      obtener = cursor.fetchall()
      return obtener
    except:
      return
    
def verifico_clave_del_mail(email):
  conexion = conexionbd()
  if conexion:
    #crear un cursor para ejecutar consultas sql
    cursor = conexion.cursor()
    
    #consulta sql para obtener contrasena del usuario con ese mail
    cursor.execute("SELECT clave FROM usuarios_web WHERE email = %s", (email,))
    
    #obtengo la clave del usuario
    obtener_clave = cursor.fetchone()
    
    return obtener_clave