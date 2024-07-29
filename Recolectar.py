import socket

# Configuración del equipo fichador
host = 'direccion_ip_del_equipo'  # Reemplazar con la IP real del dispositivo
puerto = 4370

# Crear un socket para la conexión
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Conectarse al equipo fichador
    sock.connect((host, puerto))

    # Enviar comando para descargar datos (esto puede variar según el dispositivo)
    comando = b'\x01\x00\x00\x03'  # Ejemplo de comando, podría necesitar cambios
    sock.send(comando)

    # Recibir la respuesta del equipo fichador
    respuesta = sock.recv(4096)  # Recibe hasta 4096 bytes (ajustar según necesidad)

    # Guardar la respuesta en un archivo binario
    with open('datos_fichadas.bin', 'wb') as archivo:
        archivo.write(respuesta)

    print("Datos guardados en 'datos_fichadas.bin'.")

except Exception as e:
    print(f"Error al conectar o recibir datos: {e}")

finally:
    # Cerrar la conexión
    sock.close()
