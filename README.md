<h1>Recolectores de Datos de Relojes</h1>
<p>Esta aplicación permite conectar a un dispositivo de fichaje, obtener datos de fichadas y guardarlos en un archivo CSV. La interfaz gráfica, construida con Tkinter, facilita la configuración y descarga de los datos.</p>

<h2>Requisitos</h2>
<ul>
  <li>Python 3.x</li>
  <li>Tkinter (incluido en la mayoría de las distribuciones de Python)</li>
</ul>

<h2>Instalación</h2>
<p>No se requiere instalación especial. Solo asegúrate de tener Python instalado en tu sistema. Puedes verificarlo ejecutando <code>python --version</code> en tu terminal.</p>

<h2>Uso</h2>
<p>Para ejecutar la aplicación, guarda el código en un archivo, por ejemplo, <code>recolectores_datos.py</code>. Luego, ejecuta el archivo con Python:</p>
<pre><code>python recolectores_datos.py</code></pre>
<p>La interfaz gráfica de usuario (GUI) se abrirá, permitiéndote ingresar la dirección IP del dispositivo, así como las fechas de inicio y fin para la descarga de los datos.</p>

<h3>Pasos para utilizar la aplicación:</h3>
<ol>
  <li>Ingresa la dirección IP del dispositivo de fichaje en el campo correspondiente.</li>
  <li>Especifica la fecha de inicio y fin en formato <code>YYYY-MM-DD</code>.</li>
  <li>Haz clic en "Descargar Datos".</li>
  <li>Elige la ubicación donde deseas guardar el archivo CSV que contendrá los datos de fichadas.</li>
</ol>

<h2>Detalles Técnicos</h2>
<p>La aplicación se conecta al dispositivo de fichaje utilizando un socket TCP/IP en el puerto 4370. Los comandos se envían en formato binario, y las respuestas se procesan para extraer datos de fichadas. Estos datos incluyen el nombre del dispositivo, la fecha y hora de la ficha, el legajo del empleado y el evento.</p>

<h2>Manejo de Errores</h2>
<p>La aplicación muestra mensajes de error en caso de problemas al conectar con el dispositivo o al procesar los datos. Asegúrate de que la dirección IP sea correcta y que el dispositivo esté en funcionamiento.</p>

<h2>Contribuciones</h2>
<p>Las contribuciones son bienvenidas. Si deseas mejorar la aplicación, por favor crea un fork de este proyecto y envía un pull request con tus cambios.</p>

<h2>Licencia</h2>
<p>Este proyecto está bajo la licencia MIT. Puedes utilizar, modificar y distribuir este software bajo los términos de la licencia MIT.</p>

<h2>Contacto</h2>
<p>Si tienes alguna pregunta o problema, no dudes en contactar al desarrollador a través de [correo electrónico o cualquier otro medio de contacto].</p>
