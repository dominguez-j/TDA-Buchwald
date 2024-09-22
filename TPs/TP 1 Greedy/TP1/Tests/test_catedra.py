from .. algoritmo_juego import juego_de_la_moneda as juego
from .. utils import leer_datos, ignorar_primer_linea
from . funciones_auxiliares_tests import ejecutar_test, condicion_test_valido, ruta_absoluta_tests_catedra
from os import listdir

if __name__ == '__main__':
    nombres_tests = listdir(ruta_absoluta_tests_catedra)

    for nombre in nombres_tests:
        try:
            x = int(nombre[0:nombre.index('.')])
        except:
            nombres_tests.remove(nombre)

    nombres_tests.sort(key=lambda nombre: int(nombre[0:nombre.index('.')]))

    for nombre in nombres_tests:
        arreglo_del_test = leer_datos(ruta_absoluta_tests_catedra + nombre, ignorar_primer_linea)
        ejecutar_test(juego, int(nombre[:nombre.index('.')]), condicion_test_valido, arreglo_del_test)