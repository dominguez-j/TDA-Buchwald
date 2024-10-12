from .. import algoritmo_juego
from .. utils import crear_arreglo_desordenado
from . funciones_auxiliares_tests import ejecutar_test, condicion_test_valido

if __name__ == "__main__":

    TAMAÑOS_DE_TEST = (1, 2, 3, 50, 100, 1000, 10000, 20000)

    for tamaño in TAMAÑOS_DE_TEST:
        ejecutar_test(algoritmo_juego.juego_de_la_moneda, tamaño, condicion_test_valido, crear_arreglo_desordenado(tamaño))