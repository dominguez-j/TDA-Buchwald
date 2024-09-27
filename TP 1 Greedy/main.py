import os
import tkinter as tk
from tkinter import filedialog

from TP1.algoritmo_juego import juego_de_la_moneda
from TP1.utils import leer_datos, ignorar_primer_linea

def seleccionar_archivo():
    root = tk.Tk()
    root.withdraw()
    archivo = filedialog.askopenfilename(
        title="Selecciona un archivo .txt",
        filetypes=[("Archivos de texto", "*.txt")],
        initialdir=os.getcwd())
    return archivo


if __name__ == '__main__':

    ruta_archivo = seleccionar_archivo()
    if not ruta_archivo:
        print("No se seleccionó ningún archivo.") 
    else:
        datos = leer_datos(ruta_archivo, ignorar_primer_linea)
        arreglo_sophia, _, pasos = juego_de_la_moneda(datos)
        for i in range(len(pasos)):
            if i < len(pasos) - 1:
                print(pasos[i], end='. ')
            else:
                print(pasos[i], end='.')
        print(f'\nGanancia de Sophia: {sum(arreglo_sophia)}')