import mysql.connector

class Conexion:
    def __init__(self, host, root, Root2013, projecto_integrador):
        self.host = host
        self.user = root
        self.password = Root2013
        self.database = projecto_integrador
        self.connection = None

    def connect(self):
        self.connection = mysql.connector.connect(
            host=self.host,
            root=self.user,
            Root2013=self.password,
            project_integrador=self.database
        )
        if self.connection.is_connected():
            print("Conexión exitosa")

    def disconnect(self):
        if self.connection.is_connected():
            self.connection.close()
            print("Desconexión")

    def leer_dispositivossrl(self):
        if self.connection.is_connected():
            cursor = self.connection.cursor()
            query = "SELECT * FROM projecto_integrador"
            cursor.execute(query)
            dispositivossrl = cursor.fetchall()
            cursor.close()
            return dispositivossrl
        else:
            print("No hay conexión a la base de datos")

    def ingresar_projecto_integrador(self, Number_serial, Modelo, Direccion_Instalacion, Fecha_Instalacion, Coordenadas, Id_Estado):
        if self.connection.is_connected():
            cursor = self.connection.cursor()
            query = "INSERT INTO projecto_integrador (Number_serial, Modelo, Direccion_Instalacion, Fecha_Instalacion, Coordenadas, Id_Estado) VALUES (%s, %s, %s, %s)"
            values = (Number_serial, Modelo, Direccion_Instalacion, Fecha_Instalacion, Coordenadas, Id_Estado)
            cursor.execute(query, values)
            self.connection.commit()
            cursor.close()
            print("Datos insertados correctamente")
        else:
            print("No hay conexión a la base de datos")