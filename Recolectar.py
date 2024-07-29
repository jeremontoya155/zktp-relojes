import socket
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

def descargar_datos():
    # Obtener valores de la interfaz
    host = ip_entry.get()
    puerto = 4370
    
    try:
        # Crear un socket para la conexión
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, puerto))

        # Enviar comando para descargar datos (esto puede variar según el dispositivo)
        comando = b'\x01\x00\x00\x03'  # Ejemplo de comando, podría necesitar cambios
        sock.send(comando)

        # Recibir la respuesta del equipo fichador
        respuesta = sock.recv(4096)  # Recibe hasta 4096 bytes (ajustar según necesidad)

        # Preguntar al usuario dónde guardar el archivo binario
        archivo = filedialog.asksaveasfilename(defaultextension=".bin", filetypes=[("Binary files", "*.bin")])
        if not archivo:
            return

        # Guardar la respuesta en un archivo binario
        with open(archivo, 'wb') as f:
            f.write(respuesta)

        messagebox.showinfo("Éxito", f"Datos guardados en '{archivo}'.")

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

descargar_button = tk.Button(root, text="Descargar Datos", command=descargar_datos)
descargar_button.grid(row=1, column=0, columnspan=2, pady=10)

root.mainloop()
