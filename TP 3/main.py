from TP3.Utilidades.utils_tests import RUTA_RESULTADOS, ejecutar_test
from TP3.Utilidades.utils_archivos import *

if __name__ == '__main__':
    try:
        ruta, tests_para_ejecutar = seleccionar_tests_personalizado()
        nombre = nombre_archivo(ruta)

        for algoritmo in tests_para_ejecutar:
            ruta_resultados = extender_nombre_de_archivo(nombre, RESULTADO, f'{RUTA_RESULTADOS}-{algoritmo}')
            print("------------------------------------------------------")
            print(f"Algoritmo: {algoritmo}")
            print("------------------------------------------------------")
            ejecutar_test(ruta, ruta_resultados, algoritmo)

    except Exception as e:
        print(e)