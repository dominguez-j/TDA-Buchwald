import sys
import time
import subprocess
import os

from .utils_archivos import leer_datos, guardar_datos, nombre_archivo
from .utils_generales import organizar_resultado_test, enlistar_valores, FUNCIONES_DE_FORMATEO

PARAMETRO_MOSTRAR_POR_CONSOLA = '--mostrar-por-consola'
PARAMETRO_VERIFICAR_RESULTADOS = '--verificar-resultados'
RUTA_TEST_CATEDRA = 'Ejemplos'
RUTA_RESULTADOS = 'Resultados'

def verificar_parametros_de_linea_de_comandos():
    mostrar_por_consola = False
    verificar_resultados = False
    if PARAMETRO_MOSTRAR_POR_CONSOLA in sys.argv:
        mostrar_por_consola = True
    if PARAMETRO_VERIFICAR_RESULTADOS in sys.argv:
        verificar_resultados = True
    return mostrar_por_consola, verificar_resultados

def ejecutar_algoritmo(algoritmo, valores_de_entrada):
    inicio = time.perf_counter()
    retorno = algoritmo(valores_de_entrada)
    fin = time.perf_counter()
    # Como el retorno viene desordenado, lo organizamos antes de devolverlo
    return (organizar_resultado_test(retorno, valores_de_entrada), (fin - inicio) * 1000)

def comparacion_de_resultados(ruta_resultados_obtenidos, ruta_resultados_esperados):
    try:
        # Intentamos usar el comando 'diff' en sistemas Unix (Linux, macOS)
        _ = subprocess.run(['diff', ruta_resultados_obtenidos, ruta_resultados_esperados, '-b'], check=True, capture_output=True, text=True)
        print("Los archivos son iguales.")
    except subprocess.CalledProcessError as e:
        # Si 'diff' encuentra diferencias
        print("Los archivos son diferentes:")
        print(e.stdout)
    except FileNotFoundError:
        # Si 'diff' no se encuentra, verificamos el sistema operativo
        if os.name == 'nt':  # 'nt' significa Windows
            try:
                # Intentamos usar el comando 'fc' en Windows
                _ = subprocess.run(['fc', ruta_resultados_obtenidos, ruta_resultados_esperados], check=True, capture_output=True, text=True)
                print("Los archivos son iguales.")
            except subprocess.CalledProcessError as e:
                print("Los archivos son diferentes:")
                print(e.stdout)
            except FileNotFoundError:
                print("El comando 'fc' no se encontró en Windows.")
        else:
            print("El comando 'diff' no se encontró. Asegúrate de que está instalado en tu sistema.")

def imprimir_datos_del_test(datos_del_test):
    # datos_test es un arreglo del tipo (nombre_test, ..., tiempo)
    print('Test ' + datos_del_test[0] + ': ')
    for i in range(1, len(datos_del_test) - 1):
        print(datos_del_test[i])
    print('Tiempo de ejecución: ' + str(datos_del_test[-1]) + ' milisegundos')

def resultado_test(datos_del_test, ruta_resultado_obtenido, ruta_resultado_real):
    imprimir_datos_del_test(datos_del_test)
    comparacion_de_resultados(ruta_resultado_obtenido, ruta_resultado_real)
    print(20 * '-')

def generar_resultados(algoritmo, ruta_fuente, ruta_resultados):
    valores_de_entrada = leer_datos(ruta_fuente, enlistar_valores)
    resultados, tiempo = ejecutar_algoritmo(algoritmo, valores_de_entrada)

    contenido = [nombre_archivo(ruta_fuente)]
    for dato, formateo in zip(resultados, FUNCIONES_DE_FORMATEO):
        contenido.append(formateo(dato))

    texto_final = '\n'.join(contenido)
    guardar_datos(ruta_resultados, texto_final)

    # Devolvemos el contenido por si hay que usarlo para trabajar en la función que invoca esta función
    contenido.pop(1)
    contenido.append(tiempo)
    return contenido