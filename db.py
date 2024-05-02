import pymysql
#conexion a la bd
def conexionbd():
  try:
    db = pymysql.connect(
      host='localhost',
      user='root',
      passwd='',
      database='tres_en_raya'
    )
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
  #cursor para ejecutar consultas sql, insertar nuevo usuario a la bd
  if conexion:
    cursor = conexion.cursor()
    
    #Insercion de datas a la tabla de 'usuarios_web'
    cursor.execute("INSERT INTO usuarios_web (nombre, email, clave, edad) VALUES (%s, %s, %s, %s)", (nombre, email, clave, edad))
    
    #guardar los datos en la bd
    conexion.commit()
    conexion.close() #cerrar conexion a la bd
    