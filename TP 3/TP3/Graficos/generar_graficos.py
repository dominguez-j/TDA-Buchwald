from ..Utilidades.utils_tests import correr_tests_diseñados

from ..Algoritmos.battleship_bt import battleship
from ..Algoritmos.aproximaciones_jj import battleship_aproximacion
from ..Algoritmos.battleship_greedy import battleship_greedy

from .aproximaciones import funcion_aproximadora, errores, complejidad_bt, complejidad_jj, complejidad_gd

import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

import numpy as np

def generar_grafico(x_func, y_func, z_func, x_med, y_med, z_med, eje_x_nombre, nombre_algoritmo):
    fig = plt.figure()

    ax = fig.add_subplot(111, projection = '3d')

    ax.plot(x_func, y_func, z_func, color = 'b')
    ax.scatter(x_med, y_med, z_med, label = 'puntos')

    ax.set_xlabel(eje_x_nombre)
    ax.set_ylabel('b')
    ax.set_zlabel('t')

    plt.title(nombre_algoritmo)
    plt.legend()
    plt.savefig(f'Mediciones/{nombre_algoritmo}.png')

def generar_grafico_errores(x, y, errores, ect, eje_x_nombre, nombre_algoritmo):
    fig = plt.figure()

    ax = fig.add_subplot(111, projection = '3d')

    ax.plot(x, y, errores, color = 'b')

    ax.set_xlabel(eje_x_nombre)
    ax.set_ylabel('b')
    ax.set_zlabel('t')

    plt.figtext(0.5, 0.05, f"ECT = {ect}s", ha='center', fontsize=10, color='black')

    plt.title('Error del ajuste')
    plt.legend()

    plt.savefig(f'Mediciones/{nombre_algoritmo}-errores.png')

if __name__ == '__main__':
    mediciones_bt = correr_tests_diseñados(battleship)
    mediciones_jj = correr_tests_diseñados(battleship_aproximacion)
    mediciones_gd = correr_tests_diseñados(battleship_greedy)

    puntos_bt = np.array([(med[1][0]*med[1][1], med[1][2], med[0]) for med in mediciones_bt], dtype=object)
    puntos_jj = np.array([(max(med[1][0],med[1][1]), med[1][2], med[0]) for med in mediciones_jj], dtype=object)
    puntos_gd = np.array([(max(med[1][0],med[1][1]), med[1][2], med[0]) for med in mediciones_gd], dtype=object)

    # Los parámetros de las mediciones de backtracking deben tener la forma
    #   (tiempo, (n * m, b))
    mediciones_bt = np.array([(med[0], (med[1][0] * med[1][1], med[1][2])) for med in mediciones_bt], dtype=object)
    valores_de_entrada_bt = np.array([(med[1][0], med[1][1]) for med in mediciones_bt])

    # Los de JJ y greedy tienen la forma
    #   (tiempo, (max(n, m), b))
    mediciones_jj = np.array([(med[0], (max(med[1][0], med[1][1]), med[1][2])) for med in mediciones_jj], dtype=object)
    mediciones_gd = np.array([(med[0], (max(med[1][0], med[1][1]), med[1][2])) for med in mediciones_gd], dtype=object)
    valores_de_entrada_jj_gd = np.array([(med[1][0], med[1][1]) for med in mediciones_jj])

    funcion_bt = funcion_aproximadora(complejidad_bt, mediciones_bt)
    funcion_jj = funcion_aproximadora(complejidad_jj, mediciones_jj)
    funcion_gd = funcion_aproximadora(complejidad_gd, mediciones_gd)

    Z_bt = np.array([funcion_bt(N, b) for N, b in valores_de_entrada_bt])
    Z_jj = np.array([funcion_jj(W, b) for W, b in valores_de_entrada_jj_gd])
    Z_gd = np.array([funcion_gd(W, b) for W, b in valores_de_entrada_jj_gd])

    puntos_x_bt, puntos_y_bt, puntos_z_bt = zip(*puntos_bt)
    puntos_x_jj, puntos_y_jj, puntos_z_jj = zip(*puntos_jj)
    puntos_x_gd, puntos_y_gd, puntos_z_gd = zip(*puntos_gd)

    errores_bt, ect_bt = errores(Z_bt, [med[0] for med in mediciones_bt])
    errores_jj, ect_jj = errores(Z_jj, [med[0] for med in mediciones_jj])
    errores_gd, ect_gd = errores(Z_gd, [med[0] for med in mediciones_gd])

    generar_grafico(
        puntos_x_bt,
        puntos_y_bt,
        Z_bt,
        puntos_x_bt,
        puntos_y_bt,
        puntos_z_bt,
        'N',
        'Backtracking'
    )
    generar_grafico_errores(
        puntos_x_bt,
        puntos_y_bt,
        errores_bt,
        ect_bt,
        'N',
        'Backtracking'
    )

    generar_grafico(
        puntos_x_jj,
        puntos_y_jj,
        Z_jj,
        puntos_x_jj,
        puntos_y_jj,
        puntos_z_jj,
        'W',
        'Aproximación de J.J.'
    )
    generar_grafico_errores(
        puntos_x_jj,
        puntos_y_jj,
        errores_jj,
        ect_jj,
        'W',
        'Aproximación de J.J.'
    )

    generar_grafico(
        puntos_x_gd,
        puntos_y_gd,
        Z_gd,
        puntos_x_gd,
        puntos_y_gd,
        puntos_z_gd,
        'W',
        'Greedy'
    )
    generar_grafico_errores(
        puntos_x_gd,
        puntos_y_gd,
        errores_gd,
        ect_gd,
        'W',
        'Greedy'
    )