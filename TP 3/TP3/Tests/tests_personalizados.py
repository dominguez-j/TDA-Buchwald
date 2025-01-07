from ..Utilidades.utils_archivos import extender_nombre_de_archivo
from ..Utilidades.utils_tests import generar_datos_entrada, generar_resultados, organizar_resultados, RUTA_RESULTADOS_TESTS_PERSONALIZADOS

from ..Algoritmos.battleship_bt import battleship
from ..Algoritmos.aproximaciones_jj import battleship_aproximacion
from ..Algoritmos.battleship_greedy import battleship_greedy

if __name__ == '__main__':

    algoritmos = [(battleship, "Backtracking"), (battleship_aproximacion, "Aproximación de JJ"), (battleship_greedy, "Greedy")]

    for algoritmo in algoritmos:

        for i in range(4, 27):
            generar_resultados(
                algoritmo = algoritmo[0],
                valores_de_entrada = generar_datos_entrada(i),
                organizar_datos = organizar_resultados,
                ruta_resultados = extender_nombre_de_archivo(f'{i}_{i}_{i//2}_{algoritmo[1]}.txt', '', RUTA_RESULTADOS_TESTS_PERSONALIZADOS)
            )