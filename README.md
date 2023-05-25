# ClonacionWeb
#¿Qué hace el proyecto?
Este proyecto consiste en una aplicación que permite copiar el código fuente de una página web y guardarlo en el sistema. Puede ser útil esta herramienta para obtener el código fuente de alguna página web de forma automática, la cual puede utilizarse para inspeccionar o utilizarlo sin tener el código fuente original.
También se puede utilizar para realizar pruebas reales sobre un sitio web y obtener mayor información sobre él.
# Funcionalidades
Copiar el código HTML de una página web, junto con el archivo CSS.
Obtener las imágenes del sitio web
Guarda una copia local de la página para su análisis.

# Requisitos
Para ejecutar este proyecto, necesitarás tener instalados los siguientes elementos:
Un navegador web (Google Chrome, Mozilla Firefox, etc.).
Un editor de texto o entorno de desarrollo integrado (IDE) para visualizar y editar el código en lenguaje Python.

# Tecnologías utilizadas.
Python: Para este proyecto decidimos Utilizar el lenguaje python para su desarrollo ya que cuenta con muchas características que nos facilitan la creación de este como lo son: Su gran versatilidad para diferentes aplicaciones, su sencillez es la sintaxis y su gran variedad de herramientas que se pueden aplicar
Tkinter: Es una biblioteca de Python que se utiliza para crear interfaces gráficas de usuario (GUI, por sus siglas en inglés). Proporciona una serie de herramientas y widgets que permiten diseñar ventanas, botones, cuadros de texto, menús y otros elementos visuales para construir aplicaciones de escritorio interactivas.
Shutil: Es un módulo integrado en Python que proporciona funciones para operaciones de alto nivel en archivos y directorios. Su nombre deriva de "shell utilities" (utilidades de shell), ya que su objetivo principal es proporcionar funcionalidad similar a la que se encuentra en comandos de la línea de comandos de sistemas operativos Unix.
Requests: Es una biblioteca popular y sencilla de usar para realizar solicitudes HTTP en Python. Puedes utilizarla para descargar el contenido HTML de las páginas web del sitio que deseas clonar. Puedes instalarlo utilizando pip: pip install requests.
BeautifulSoup: Es una biblioteca para analizar y extraer datos de documentos HTML y XML. Puedes utilizarlo en combinación con Requests para extraer información específica del sitio web clonado, como enlaces, imágenes o texto. Puedes instalarlo utilizando pip: pip install beautifulsoup4.
urllib.parse: Es un módulo en Python que proporciona funciones para analizar y manipular URLs. Este módulo es parte de la biblioteca estándar de Python, por lo que no es necesario instalar ninguna biblioteca adicional para utilizarlo.
urlparse: Analiza una URL y la descompone en sus componentes (esquema, nombre de dominio, ruta, parámetros de consulta, fragmento, etc.).
urljoin: Combina dos URLs para crear una URL absoluta bien formada.

# Instrucciones de Uso
1. Abre el navegador web de tu preferencia y accede a la página web que deseas copiar.
2. Accede al siguiente enlace: https://github.com/hugoheldens/ClonacionWeb
3. Dentro del repositorio, haz clic en el archivo clonacionWebV4.py.
4. Una vez dentro del archivo, darás clic en las opciones y luego dar clic en Download
5. Una vez descargado el archivo, abres el archivo con el IDE de tu preferencia.
6. Una vez dentro del IDE, ejecutarás este archivo.
7. Después de ejecutar el archivo, observarás la siguiente ventana.


Esta ventana es la interfaz del programa. Dentro de esta misma, en el apartado de URL, colocarás la URL de la página que deseas copiar.
Después de esto, podrás seleccionar la casilla de Mostrar mas detalles. Si la casilla esta marcada, mostrará detalles de los archivos que se estan descargando:

De lo contrario, solo mostrará un mensaje después de que se termine de copiar la página web.

Después de haber seleccionado o no la casilla de Mostrar mas detalles, y dar clic en el botón de Clonar se abrirá una ventana para seleccionar la carpeta destino donde se almacenarán los archivos descargados y se dará clic en Seleccionar Carpeta.



A continuación se empezarán a descargar los archivos de la página web, y se mostrará el mensaje Clonado completo una vez terminadas las descargas.

Por último, puede acceder a la carpeta que seleccionó anteriormente, y observará una carpeta con todos los archivos de forma local.

¡Listo! Puede abrir la página de forma local. Esto lo podrás confirmar, ya que dentro de la URL se encuentra la dirección local de donde se encuentran los archivos.

# Créditos
El código fue creado por alumnos de la Facultad de Estudios Superiores Aragón:
Fernández Ávila Hugo
Hidalgo Lara Jared
Machorro Chávez Augusto Francisco
Vega Trejo Javier Raymundo

# ¿Por qué el proyecto es útil?
Desde un punto de vista completamente legal la clonación de sitios tiene diversas utilidades para diversos casos como los siguientes
Realización de copias de seguridad o recuperación: Se puede dar el caso ene cual no podamos tener acceso directo a los archivos de los que se compone nuestro sitio y mediante la clonación podemos obtener una copia de estos
. Migración del sitio: En el caso de que se tenga que mover un sitio a otro servidor, la clonación es una herramienta que nos ayudaría bastante la transferencia
. Pruebas y Desarrollo: Al querer realizar cambios o pruebas a nuestro sitio podemos realizar un clonado para así crear un entorno aparte en el cual modifiquemos nuestro sitio sin afectar lo directamente.

