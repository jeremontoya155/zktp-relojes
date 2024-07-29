import socket
import struct
import datetime
import csv
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

def descargar_datos():
    # Obtener valores de la interfaz
    host = ip_entry.get()
    puerto = 4370
    fecha_inicio = datetime.datetime.strptime(fecha_inicio_entry.get(), '%Y-%m-%d')
    fecha_fin = datetime.datetime.strptime(fecha_fin_entry.get(), '%Y-%m-%d')
    
    try:
        # Crear un socket para la conexión
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, puerto))

        # Enviar comando para obtener el nombre del dispositivo
        comando = b'\x01\x00\x00\x02'
        sock.send(comando)
        respuesta = sock.recv(1024)
        nombre_dispositivo = respuesta[4:].decode('utf-8')
        print(f"Nombre del dispositivo: {nombre_dispositivo}")

        # Preguntar al usuario dónde guardar el archivo CSV
        archivo = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
        if not archivo:
            return

        # Crear archivo CSV para guardar los datos
        with open(archivo, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Dispositivo', 'Fecha', 'Hora', 'Legajo', 'Evento'])

            # Enviar comando para descargar datos de fichadas
            comando = struct.pack('BBHHHHHH', 0x01, 0x00, 0x00, 0x03,
                                  fecha_inicio.year, fecha_inicio.month, fecha_inicio.day,
                                  fecha_inicio.hour, fecha_inicio.minute, fecha_inicio.second,
                                  fecha_fin.year, fecha_fin.month, fecha_fin.day,
                                  fecha_fin.hour, fecha_fin.minute, fecha_fin.second)
            sock.send(comando)
            respuesta = sock.recv(1024)

            # Procesar la respuesta
            record_size = 7  # 2 bytes legajo, 4 bytes timestamp, 1 byte evento
            for i in range(0, len(respuesta), record_size):
                record = respuesta[i:i+record_size]
                
                # Desempaquetar los datos según el formato
                legajo, timestamp, evento = struct.unpack('H I B', record[:7])
                
                # Convertir timestamp Unix a fecha y hora
                fecha_hora = datetime.datetime.fromtimestamp(timestamp)
                
                # Escribir datos en el archivo CSV
                writer.writerow([nombre_dispositivo, fecha_hora.date(), fecha_hora.time(), legajo, evento])

        messagebox.showinfo("Éxito", "Datos descargados con éxito.")
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo conectar o recibir datos: {e}")
    finally:
        sock.close()

# Crear la interfaz gráfica
root = tk.Tk()
root.title("Descargar Datos de Fichadas")

tk.Label(root, text="Dirección IP del dispositivo:").grid(row=0, column=0, padx=5, pady=5)
ip_entry = tk.Entry(root)
ip_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Fecha de inicio (YYYY-MM-DD):").grid(row=1, column=0, padx=5, pady=5)
fecha_inicio_entry = tk.Entry(root)
fecha_inicio_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="Fecha de fin (YYYY-MM-DD):").grid(row=2, column=0, padx=5, pady=5)
fecha_fin_entry = tk.Entry(root)
fecha_fin_entry.grid(row=2, column=1, padx=5, pady=5)

descargar_button = tk.Button(root, text="Descargar Datos", command=descargar_datos)
descargar_button.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()
