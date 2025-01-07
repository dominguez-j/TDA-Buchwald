import numpy as np

from math import log2


# Las funciones que vamos a ajustar son de varias variables y no linealizables.
# Debido a esto, vamos a aplicar una acercamiento para el ajuste por cuadrados
# mínimos usando técnicas de modelación numérica, aplicando productos internos
# discretos.

def complejidad_bt(N, b): # N = n * m
    return (1.44)**b

def complejidad_jj(W, b): # W = max(n, m)
    return W**3

def complejidad_gd(W, b):
    return W**3

def producto_interno_discreto(f: list, g: list):

    # Las listas f y g contienen los valores de la función real
    # evaluados en determinados puntos (a, b). El producto interno
    # discreto consiste en sumar los productos
    # 
    #   f(a_i, b_i) · g(a_i, b_i)

    return np.dot(f, g)

def determinar_coeficiente(funcion, mediciones):

    # Vamos a ajustar la función por la siguiente función aproximadora
    #
    #   f*(a, b) = c · g(a, b)
    #
    # Donde g(a, b) es el parámetro 'funcion'.

    # Obtenemos los resultados de las mediciones, que son el primer
    # elemento del arreglo 'mediciones'

    resultados_medidos = np.array([medicion[0] for medicion in mediciones])

    # Ahora obtenemos las evaluaciones de 'funcion' en los parámetros
    # de las mediciones

    resultados_funcion = np.array([funcion(m[1][0], m[1][1]) for m in mediciones])

    # Ahora van a hacer falta dos productos internos discretos.
    # Como solo hay una función en el desarrollo de f*, se puede
    # plantear el ajuste por CM como una matriz de 1 × 1, con un
    # único coeficiente (c) e igualado a un vector de una fila.
    #
    # El sistema tiene la siguiente forma:
    #
    #   [ (g, g)_d ] [c] = [ (g, f)_d ]
    #
    # Con (a, b)_d el producto interno discreto. Entonces, hacen falta
    # estos PID

    pid_gg = producto_interno_discreto(resultados_funcion, resultados_funcion)
    pid_gf = producto_interno_discreto(resultados_medidos, resultados_funcion)

    # El coeficiente se despeja directamente

    return pid_gf / pid_gg

def errores(resultados_aproximacion: np.array, resultados_mediciones: np.array) -> np.array:
    errores = resultados_aproximacion - resultados_mediciones
    error_cuadratico_total = np.sum([error ** 2 for error in errores])
    return errores, error_cuadratico_total

def funcion_aproximadora(funcion_original, mediciones):
    coeficiente = determinar_coeficiente(funcion_original, mediciones)

    return lambda a, b: coeficiente * funcion_original(a, b)