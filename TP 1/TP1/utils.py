import csv
import time
import random

def leer_datos(ruta, operacion_sobre_linea):
    datos = []
    try:
        with open(ruta, mode = 'r') as archivo:
            for linea in archivo:
                resultado_de_operacion = operacion_sobre_linea(linea)
                if resultado_de_operacion is not None:
                    datos.extend(resultado_de_operacion)
        return datos
    except:
        print(f"Hubo un problema al leer la información de la siguiente ruta: {ruta}")
        raise Exception()

def guardar_datos(ruta, datos): # Los datos almacenados se guardan en archivos de extensión .csv
    try:
        with open(ruta, mode = 'w', newline = '', encoding = 'utf-8') as archivo:
            escritor = csv.writer(archivo)
            escritor.writerows(datos)
    except:
        print("Hubo un problema al guardar la información de la siguiente ruta:", ruta)

def ignorar_primer_linea(linea: str):
    if linea[0] != '#':
        return [int(elemento) for elemento in linea.strip().split(';')]
    return None

def tomar_tiempo(funcion, argumento):
    inicio = time.perf_counter()
    retorno = funcion(argumento)[:2]
    fin = time.perf_counter()
    return (retorno, (fin - inicio) * 1000)

def crear_arreglo_desordenado(cantidad_elementos):
    random.seed(0) # Se fija la semilla para que las entradas sean reproducibles
    arreglo = [i for i in range(1, cantidad_elementos + 1)]
    random.shuffle(arreglo)
    return arreglo