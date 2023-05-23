# -*- coding: utf-8 -*-
"""
Created on Mon May 22 23:43:36 2023

@author: Jared HL
"""

import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
import os
import shutil
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk


def clonar_sitio_web():
    url = url_entry.get()

    # Configurar las cabeceras del navegador
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        'Referer': url
    }

    # Realizar la solicitud HTTP con las cabeceras
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        html = response.text
    except requests.exceptions.RequestException as e:
        result_label.config(text="Error al acceder a la URL")
        return

    # Crear un objeto BeautifulSoup para analizar el HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Seleccionar el directorio de destino
    directorio_destino = filedialog.askdirectory()
    if not directorio_destino:
        result_label.config(text="No se seleccionó un directorio de destino")
        return

    # Descargar y guardar cada archivo enlazado encontrado en el sitio web
    descargar_archivos(soup, url, directorio_destino)

    result_label.config(text="Clonado completado!")


def descargar_archivos(soup, url, directorio_destino):
    # Obtener todos los enlaces encontrados en el sitio web
    enlaces = soup.find_all(['a', 'img', 'link', 'script', 'source', 'embed', 'iframe', 'object', 'video', 'audio'])

    total_archivos = len(enlaces)
    progreso = 0

    # Crear la barra de progreso
    progress_bar = ttk.Progressbar(window, maximum=total_archivos, length=300)
    progress_bar.pack()

    for enlace in enlaces:
        href = enlace.get('href')
        src = enlace.get('src')
        if href:
            # Convertir el enlace relativo a enlace absoluto
            enlace_absoluto = urljoin(url, href)

            # Descargar el archivo solo si pertenece al mismo dominio
            if urlparse(enlace_absoluto).netloc == urlparse(url).netloc:
                descargar_archivo(enlace_absoluto, directorio_destino)

        if src:
            # Convertir la ruta relativa a ruta absoluta
            src_absoluto = urljoin(url, src)

            # Descargar el archivo solo si pertenece al mismo dominio
            if urlparse(src_absoluto).netloc == urlparse(url).netloc:
                descargar_archivo(src_absoluto, directorio_destino)

        # Actualizar el progreso de la barra
        progreso += 1
        progress_bar['value'] = progreso
        window.update()

    # Eliminar la barra de progreso al completar la descarga
    progress_bar.destroy()


def descargar_archivo(url, directorio_destino):
    # Configurar las cabeceras del navegador
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        'Referer': url
    }

    # Realizar la solicitud HTTP con las cabeceras
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        # Obtener el nombre del archivo de la URL
        nombre_archivo = os.path.basename(urlparse(url).path)

        # Verificar si es un directorio y omitir la descarga
        if not nombre_archivo:
            return

        # Obtener la ruta relativa del archivo
        ruta_relativa = urlparse(url).path

        # Crear la estructura de carpetas correspondiente en el directorio destino
        ruta_absoluta = os.path.join(directorio_destino, ruta_relativa.lstrip("/"))
        directorio = os.path.dirname(ruta_absoluta)
        os.makedirs(directorio, exist_ok=True)

        # Guardar el archivo en la ruta absoluta
        with open(ruta_absoluta, 'wb') as archivo:
            archivo.write(response.content)
    except requests.exceptions.RequestException as e:
        print("Error al descargar el archivo:", url, str(e))


# Crear la ventana principal
window = tk.Tk()
window.title("Clonador de Sitios Web")

# Etiqueta y campo de entrada para la URL
url_label = tk.Label(window, text="URL:")
url_label.pack()
url_entry = tk.Entry(window, width=50)
url_entry.pack()

# Botón de clonar
clone_button = tk.Button(window, text="Clonar", command=clonar_sitio_web)
clone_button.pack()

# Etiqueta para mostrar el resultado
result_label = tk.Label(window, text="")
result_label.pack()

# Iniciar el bucle de eventos de la ventana
window.mainloop()
