import tkinter as tk
from tkinter import filedialog
import os

RESULTADO = "_resultado"
RESULTADO_REAL = "_resultado_real"

def seleccionar_archivo_de_entrada():
    raiz = tk.Tk()
    raiz.withdraw()
    ruta = filedialog.askopenfilename(
        title = "Selecciona un archivo .txt",
        filetypes = [("Archivos de texto", "*.txt")],
        initialdir = os.getcwd()
    )
    return ruta

def leer_datos(ruta, operacion_sobre_linea):
    datos = []
    try:
        with open(ruta, mode = 'r') as archivo:
            for linea in archivo:
                if not verificar_comentario(linea):
                    datos.extend(operacion_sobre_linea(linea))
        return datos
    except:
        raise Exception(f"Hubo un problema al leer la información de la siguiente ruta: {ruta}")

def guardar_datos(ruta, contenido):
    try:
        with open(ruta, mode = 'w', newline = '', encoding = 'utf-8') as archivo:
            archivo.write(contenido)
    except:
        Exception(f"Hubo un problema al guardar la información de la siguiente ruta: {ruta}")

def nombre_archivo(ruta):
    return os.path.basename(ruta)

def nombre_archivo_separado(ruta):
    nombre_separado = list(os.path.splitext(ruta))
    nombre_separado[0] = nombre_archivo(nombre_separado[0])
    return tuple(nombre_separado)

def directorio_archivo(ruta):
    return os.path.dirname(ruta)

def extender_nombre_de_archivo(ruta, sufijo = "", nuevo_directorio = ""):
    nombre_separado = nombre_archivo_separado(ruta)
    if nuevo_directorio == "":
        nuevo_directorio = directorio_archivo(ruta)
    return os.path.join(nuevo_directorio, f"{nombre_separado[0]}{sufijo}{nombre_separado[1]}")

def verificar_comentario(linea):
    if linea[0] == '#':
        return True
    return False