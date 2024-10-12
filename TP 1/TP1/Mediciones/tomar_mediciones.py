from .. algoritmo_juego import juego_de_la_moneda as juego
from .. utils import tomar_tiempo, crear_arreglo_desordenado, guardar_datos
from . funciones_auxiliares_mediciones import ruta_absoluta_resultados

if __name__ == '__main__':
    tamaños_de_entrada = [i for i in range(5000, 100000 +1, 5000)]
    mediciones = []

    for tamaño in tamaños_de_entrada:
        mediciones.append([tamaño, tomar_tiempo(juego, crear_arreglo_desordenado(tamaño))[-1]])

    guardar_datos(ruta_absoluta_resultados, mediciones)