import time
from .utils_archivos import agrupar_datos, leer_datos, guardar_datos, nombre_archivo, seleccionar_archivo_de_entrada
from .utils_generales import organizar_resultados
from ..Algoritmos import aproximaciones_jj, battleship_bt, battleship_greedy

RUTA_TEST_CATEDRA = 'Ejemplos'
RUTA_RESULTADOS = 'Resultados'
RUTA_RESULTADOS_TESTS_PERSONALIZADOS = 'Tests-Personalizados'

def ejecutar_algoritmo(algoritmo, valores_de_entrada, organizar_datos):
    inicio = time.perf_counter()
    retorno = algoritmo(*valores_de_entrada)
    fin = time.perf_counter()

    if organizar_datos is None:
        return fin - inicio

    return (organizar_datos(retorno, valores_de_entrada), (fin - inicio))

def generar_resultados(*, algoritmo, valores_de_entrada, organizar_datos, ruta_fuente = '', ruta_resultados):
    resultados, tiempo = ejecutar_algoritmo(algoritmo, valores_de_entrada, organizar_datos)

    contenido = [nombre_archivo(ruta_fuente)] if ruta_fuente != '' else []
    for dato in resultados:
        contenido.append(dato)

    contenido = ''.join(contenido)
    guardar_datos(ruta_resultados, contenido)

    return f'{contenido}\n\nTiempo de ejecución: {tiempo}\n\n'

def ejecutar_test(ruta, ruta_resultados, algoritmo):

    valores_de_entrada = leer_datos(ruta, agrupar_datos)

    if algoritmo == "Backtracking":
        print(generar_resultados(
            algoritmo = battleship_bt.battleship,
            valores_de_entrada = valores_de_entrada,
            organizar_datos = organizar_resultados,
            ruta_fuente = ruta,
            ruta_resultados = ruta_resultados
        ))
    elif algoritmo == "Aproximación de JJ":
        print(generar_resultados(
            algoritmo = aproximaciones_jj.battleship_aproximacion,
            valores_de_entrada = valores_de_entrada,
            organizar_datos = organizar_resultados,
            ruta_fuente = ruta,
            ruta_resultados = ruta_resultados
        ))
    elif algoritmo == "Greedy":
        print(generar_resultados(
            algoritmo = battleship_greedy.battleship_greedy,
            valores_de_entrada = valores_de_entrada,
            organizar_datos = organizar_resultados,
            ruta_fuente = ruta,
            ruta_resultados = ruta_resultados
        ))

def generar_datos_entrada(tamaño):
    return ([tamaño for i in range(tamaño)], [tamaño for i in range(tamaño)], [tamaño//2 for i in range(tamaño//2)])

def tomar_medicion(algoritmo, valores_de_entrada):

    tiempo = ejecutar_algoritmo(algoritmo, valores_de_entrada, None)

    return (tiempo, list(map(lambda v: len(v), valores_de_entrada)))

def correr_tests_diseñados(algoritmo):

    mediciones = []

    for i in range(4, 27):
        mediciones.append(tomar_medicion(algoritmo, generar_datos_entrada(i)))

    return mediciones