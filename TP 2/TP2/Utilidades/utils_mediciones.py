import random
from .. juego_de_las_monedas import resultado_del_juego as juego
from .. Utilidades.utils_tests import ejecutar_algoritmo

RUTA_GRAFICO_MEDICION_REAL = 'TP2/Mediciones/grafico_medicion_real.png'
RUTA_GRAFICO_COMPARACION = 'TP2/Mediciones/grafico_comparacion.png'
RUTA_GRAFICO_ERRORES = 'TP2/Mediciones/grafico_errores.png'

def tomar_mediciones():
    tamaños_de_entrada = [i for i in range(1000, 10000 +1, 1000)]
    mediciones = []

    for tamaño in tamaños_de_entrada:
        mediciones.append([tamaño, ejecutar_algoritmo(juego, crear_arreglo_desordenado(tamaño))[-1]])

    return mediciones

def crear_arreglo_desordenado(cantidad_elementos):
    random.seed(0) # Se fija la semilla para que las entradas sean reproducibles
    arreglo = [i for i in range(1, cantidad_elementos + 1)]
    random.shuffle(arreglo)
    return arreglo