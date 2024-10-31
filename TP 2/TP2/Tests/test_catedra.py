from .. juego_de_las_monedas import resultado_del_juego
from .. Utilidades.utils_archivos import extender_nombre_de_archivo, RESULTADO, RESULTADO_REAL
from .. Utilidades.utils_tests import generar_resultados, RUTA_TEST_CATEDRA, RUTA_RESULTADOS, resultado_test
from os import listdir

if __name__ == '__main__':
    nombres_tests = listdir(RUTA_TEST_CATEDRA)

    # Ordenamos los test por tamaño
    nombres_tests.sort(key=lambda nombre: int(nombre[0:nombre.index('.')]))

    for nombre in nombres_tests:
        # La ruta donde están los test de la cátedra
        ruta = extender_nombre_de_archivo(nombre, '', RUTA_TEST_CATEDRA)

        # La ruta para cada resultado
        ruta_resultados = extender_nombre_de_archivo(nombre, RESULTADO, RUTA_RESULTADOS)

        # La ruta del resultado esperado de cada test
        ruta_resultados_reales = extender_nombre_de_archivo(nombre, RESULTADO_REAL, RUTA_RESULTADOS)

        # Guardamos los resultados en un archivo y los devolvemos para imprimirlos
        resultado = generar_resultados(resultado_del_juego, ruta, ruta_resultados)

        # Se encarga de comparar los resultados reales con los obtenidos e imprime
        # las ganancias de Sophia y Mateo y el tiempo de ejecución en milisegundos
        resultado_test(resultado, ruta_resultados, ruta_resultados_reales)