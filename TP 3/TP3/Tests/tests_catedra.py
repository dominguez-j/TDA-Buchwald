from ..Utilidades.utils_archivos import extender_nombre_de_archivo, RESULTADO
from ..Utilidades.utils_tests import RUTA_TEST_CATEDRA, RUTA_RESULTADOS, ejecutar_test
from os import listdir

if __name__ == '__main__':
    nombres_tests = listdir(RUTA_TEST_CATEDRA)

    for algoritmo in ["Backtracking", "Greedy", "Aproximación de JJ"]:
        print("------------------------------------------------------")
        print(f"Algoritmo: {algoritmo}")
        print("------------------------------------------------------")
        for nombre in nombres_tests:
            # La ruta donde están los test de la cátedra
            ruta = extender_nombre_de_archivo(nombre, '', RUTA_TEST_CATEDRA)

            # La ruta para cada resultado
            ruta_resultados = extender_nombre_de_archivo(nombre, RESULTADO, f'{RUTA_RESULTADOS}-{algoritmo}')

            ejecutar_test(ruta, ruta_resultados, algoritmo)