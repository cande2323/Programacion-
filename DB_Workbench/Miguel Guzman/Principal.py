import mysql.connector

# Conectarse a la base de datos
db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Root2013",
  database="proyectov1"
)

# Método para actualizar un dispositivo
def actualizar_dispositivo(Modelo, Numero_Serial, Direccion_Instalacion, Fecha_Instalacion, Coordenadas, Id_Estado):
    cursor = db.cursor()
    sql = "UPDATE Dispositivos SET ModeloId=%s, EstadoId=%s, NumeroSerie=%s, DireccionInstalacion=%s, FechaInstalacion=%s, Coordenadas=%s WHERE Id=%s"
    values = (Modelo, Numero_Serial, Direccion_Instalacion, Fecha_Instalacion, Coordenadas, Id_Estado)
    cursor.execute(sql, values)
    db.commit()
    print("Dispositivo actualizado correctamente")

# Método para eliminar un dispositivo
def eliminar_dispositivo(id):
    cursor = db.cursor()
    sql = "DELETE FROM Dispositivos WHERE Id=%s"
    value = (Modelo,)
    cursor.execute(sql, value)
    db.commit()
    print("Dispositivo eliminado correctamente")

# Método para mostrar el menú
def mostrar_menu():
    print("------- MENÚ -------")
    print("1. Actualizar dispositivo")
    print("2. Eliminar dispositivo")
    print("3. Salir")
    print("--------------------")

# Ciclo principal del programa
while True:
    mostrar_menu()
    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        Modelo = int(input("Ingrese el nuevo ID del modelo: "))
        Id_Estado = int(input("Ingrese el nuevo ID del estado: "))
        Numero_Serial = input("Ingrese el nuevo número de serie: ")
        Direccion_Instalacion = input("Ingrese la nueva dirección de instalación: ")
        Fecha_Instalacion = input("Ingrese la nueva fecha de instalación (YYYY-MM-DD): ")
        Coordenadas = input("Ingrese las nuevas coordenadas: ")
        actualizar_dispositivo(Modelo, Numero_Serial, Direccion_Instalacion, Fecha_Instalacion, Coordenadas)
    elif opcion == "2":
        Modelo = int(input("Ingrese el ID del dispositivo a eliminar: "))
        eliminar_dispositivo(Modelo)
    elif opcion == "3":
        break
    else:
        print("Opción inválida. Por favor, ingrese una opción válida.")

# Cerrar la conexión a la base de datos
db.close()