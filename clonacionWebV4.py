# -*- coding: utf-8 -*-
"""
Created on Tue May 23 23:36:52 2023

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
from tkinter.scrolledtext import ScrolledText

def clonar_sitio_web():
    global enlaces_visitados

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
        append_to_log("Error al acceder a la URL")
        return

    # Crear un objeto BeautifulSoup para analizar el HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Seleccionar el directorio de destino
    directorio_destino = filedialog.askdirectory()
    if not directorio_destino:
        append_to_log("No se seleccionó un directorio de destino")
        return

    # Inicializar el conjunto de enlaces visitados
    enlaces_visitados = set()

    # Realizar el spidering y descargar los archivos
    spidering(soup, url, directorio_destino)

    append_to_log("Clonado completado!")

def spidering(soup, url, directorio_destino):
    global enlaces_visitados

    # Obtener todos los enlaces encontrados en el sitio web
    enlaces = soup.find_all(['a', 'img', 'link', 'script', 'source', 'embed', 'iframe', 'object', 'video', 'audio'])

    total_enlaces = len(enlaces)
    progreso = ttk.Progressbar(window, length=200, mode='determinate', maximum=total_enlaces)
    progreso.pack()

    mostrar_detalles = detalles_var.get()

    for i, enlace in enumerate(enlaces):
        href = enlace.get('href')
        src = enlace.get('src')
        if href:
            # Convertir el enlace relativo a enlace absoluto
            enlace_absoluto = urljoin(url, href)

            # Descargar el archivo solo si pertenece al mismo dominio y no ha sido visitado previamente
            if urlparse(enlace_absoluto).netloc == urlparse(url).netloc and enlace_absoluto not in enlaces_visitados:
                descargar_archivo(enlace_absoluto, directorio_destino)
                enlaces_visitados.add(enlace_absoluto)
                if mostrar_detalles:
                    append_to_log(f"Descargando {enlace_absoluto}")
                progreso['value'] = i + 1
                window.update()

                # Realizar spidering en el enlace visitado
                spider_enlace(enlace_absoluto, directorio_destino)

        if src:
            # Convertir la ruta relativa a ruta absoluta
            src_absoluto = urljoin(url, src)

            # Descargar el archivo solo si pertenece al mismo dominio y no ha sido visitado previamente
            if urlparse(src_absoluto).netloc == urlparse(url).netloc and src_absoluto not in enlaces_visitados:
                descargar_archivo(src_absoluto, directorio_destino)
                enlaces_visitados.add(src_absoluto)
                if mostrar_detalles:
                    append_to_log(f"Descargando {src_absoluto}")
                progreso['value'] = i + 1
                window.update()

                # Realizar spidering en el enlace visitado
                spider_enlace(src_absoluto, directorio_destino)

    progreso.destroy()

def spider_enlace(url, directorio_destino):
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
        append_to_log("Error al acceder a la URL: " + url)
        return

    # Crear un objeto BeautifulSoup para analizar el HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Realizar el spidering y descargar los archivos
    spidering(soup, url, directorio_destino)

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
        append_to_log("Error al descargar el archivo: " + url)

def append_to_log(message):
    log_text.insert(tk.END, message + "\n")
    log_text.see(tk.END)

# Crear la ventana principal
window = tk.Tk()
window.title("Clonador de Sitios Web")

# Etiqueta y campo de entrada para la URL
url_label = tk.Label(window, text="URL:")
url_label.pack()
url_entry = tk.Entry(window, width=50)
url_entry.pack()

# Opción desplegable para mostrar más detalles
detalles_var = tk.BooleanVar()
detalles_checkbox = tk.Checkbutton(window, text="Mostrar más detalles", variable=detalles_var)
detalles_checkbox.pack()

# Botón de clonar
clone_button = tk.Button(window, text="Clonar", command=clonar_sitio_web)
clone_button.pack()

# Recuadro de texto para mostrar el log
log_text = ScrolledText(window, height=10, width=80)
log_text.pack()

# Iniciar el bucle de eventos de la ventana
window.mainloop()
