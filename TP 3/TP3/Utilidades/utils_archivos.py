import tkinter as tk
from tkinter import filedialog, messagebox
import os

RESULTADO = "_resultado"

def seleccionar_archivo_de_entrada():
    raiz = tk.Tk()
    raiz.withdraw()
    ruta = filedialog.askopenfilename(
        title = "Selecciona un archivo .txt",
        filetypes = [("Archivos de texto", "*.txt")],
        initialdir = os.getcwd()
    )
    if not ruta:
        messagebox.showwarning("Advertencia", "No se seleccionó ningún archivo.")
    return ruta

def seleccionar_tests_personalizado():
    ruta = seleccionar_archivo_de_entrada()

    ventana = tk.Tk()
    ventana.title("Seleccionar Algoritmo")
    ventana.geometry("400x240")

    algoritmos_a_ejecutar = []

    def bt():
        algoritmos_a_ejecutar.append("Backtracking")
        ventana.destroy()
    def jj():
        algoritmos_a_ejecutar.append("Aproximación de JJ")
        ventana.destroy()
    def gd():
        algoritmos_a_ejecutar.append("Greedy")
        ventana.destroy()
    def todos():
        algoritmos_a_ejecutar.extend(["Backtracking", "Aproximación de JJ", "Greedy"])
        ventana.destroy()

    etiqueta = tk.Label(ventana, text="Selecciona un algoritmo para correr los tests:", font=("Arial", 14))
    etiqueta.pack(pady=10)

    boton_bt = tk.Button(ventana, text="Backtracking", command=bt, font=("Arial", 12))
    boton_bt.pack(pady=5)

    boton_jj = tk.Button(ventana, text="Aproximación de J.J.", command=jj, font=("Arial", 12))
    boton_jj.pack(pady=5)

    boton_greedy = tk.Button(ventana, text="Greedy", command=gd, font=("Arial", 12))
    boton_greedy.pack(pady=5)

    boton_todos = tk.Button(ventana, text="Ejecutar todos los algoritmos", command=todos, font=("Arial", 12))
    boton_todos.pack(pady=5)

    ventana.wait_window()

    return ruta, algoritmos_a_ejecutar

def leer_datos(ruta, organizacion_de_datos):
    datos = [[]]
    try:
        with open(ruta, mode = 'r') as archivo:
            for linea in archivo:
                if not verificar_comentario(linea):
                    organizacion_de_datos(datos, linea)
        return datos
    except:
        raise Exception(f"Hubo un problema al leer la información de la siguiente ruta: {ruta}")

def guardar_datos(ruta, contenido):
    try:
        directorio = os.path.dirname(ruta)
        
        # Crear el directorio si no existe
        if directorio and not os.path.exists(directorio):
            os.makedirs(directorio)
        
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

def agrupar_datos(datos, linea):
    if linea == '\n':
        datos.append([])
    else:
        datos[-1].append(int(linea))