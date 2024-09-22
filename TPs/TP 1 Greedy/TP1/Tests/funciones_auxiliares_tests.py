from .. utils import tomar_tiempo

ruta_absoluta_tests_catedra = 'Ejemplos/'

def condicion_test_valido(monedas_de_los_hermanos):
    # monedas_de_los_hermanos[0] == monedas_de_sofia, monedas_de_los_hermanos[1] == monedas_de_mateo
    return sum(monedas_de_los_hermanos[0]) > sum(monedas_de_los_hermanos[1])

def resultado_test(tamaño_del_test, validacion_test, resultado, tiempo):
    print('Test de ' + str(tamaño_del_test) + ' moneda(s)' + ': ', end='')
    if validacion_test(resultado):
        print('\u2714')
    else:
        print('\u274C')
    print('Tiempo de ejecución: ' + str(tiempo) + ' mili sec')
    print(20 * '-')

def ejecutar_test(funcion, tamaño_del_test, validacion_test, arreglo):
    resultado_test(tamaño_del_test, validacion_test, *tomar_tiempo(funcion, arreglo))