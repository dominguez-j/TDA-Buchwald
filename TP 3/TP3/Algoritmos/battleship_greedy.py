import heapq as heap
from ..Utilidades.utils_generales import AGUA

def heapificar_demandas(demandas): # O(W log(W))
    heap_max = []
    for i, d in enumerate(demandas):
        if d != 0:
            heap.heappush(heap_max, (-d, i))  # O(log(W)
    return heap_max

def ocupada(tablero, casilla): # O(1)
    return tablero[casilla[0]][casilla[1]] != AGUA

def adyacentes_a_casilla(tablero, casilla): # O(1)
    adyacentes = []
    for i in range(casilla[0] - 1, casilla[0] + 2):
        for j in range(casilla[1] - 1, casilla[1] + 2):
            if i >= 0 and j >= 0 and i < len(tablero) and j < len(tablero[0]) and (i, j) != casilla:
                adyacentes.append((i, j))
    return adyacentes

def adyacentes_libres(tablero, posicion, alto, ancho): # O(W)

    casillas = [(posicion[0] + i, posicion[1] + j) for i in range(alto) for j in range(ancho)]

    for casilla in casillas:
        adyacentes = adyacentes_a_casilla(tablero, casilla)
        for adyacente in adyacentes:
            if adyacente not in casillas:
                if ocupada(tablero, adyacente):
                    return False
    return True

def demandas_validas(d_filas, d_cols, posicion, alto, ancho): # O(W)
    d_filas_actualizadas = {}
    d_cols_actualizadas = {}

    for i in range(posicion[0], posicion[0] + alto):
        for j in range(posicion[1], posicion[1] + ancho):
            if i >= len(d_filas) or j >= len(d_cols):
                return False

            if i not in d_filas_actualizadas:
                d_filas_actualizadas[i] = d_filas[i]
            d_filas_actualizadas[i] -= 1

            if j not in d_cols_actualizadas:
                d_cols_actualizadas[j] = d_cols[j]
            d_cols_actualizadas[j] -= 1

            if d_filas_actualizadas[i] < 0 or d_cols_actualizadas[j] < 0:
                return False

    return True

def posicion(tablero, d_filas, d_cols, barco, demanda): # O(W W)
    indice = demanda[1]
    lado_mas_largo = max(barco[0], barco[1])
    longitud_maxima = len(tablero) if barco[0] == 1 else len(tablero[0])

    if demanda[0] < lado_mas_largo:
        return None

    for i in range(longitud_maxima - lado_mas_largo):
        pos_inicio = (indice, i) if barco[0] == 1 else (i, indice)

        no_tiene_adyacentes = adyacentes_libres(tablero, pos_inicio, barco[0], barco[1])
        no_excede_demandas = demandas_validas(d_filas, d_cols, pos_inicio, barco[0], barco[1])
        posicion_valida = no_tiene_adyacentes and no_excede_demandas

        if posicion_valida:
            return pos_inicio

    return None

def calcular_sobrante(demanda, barco): # O(1)
    return -demanda[0] - barco[0]

def encontrar_mejor_demanda(tablero, d_filas, d_cols, barco, d_filas_heap, d_cols_heap): # O(W W W)
    mejor_demanda = None
    mejor_posicion = None
    menor_sobrante = float('inf')
    mejor_orientacion = None

    for demanda in d_filas_heap:
        valor_negado, indice = demanda
        valor = -valor_negado
        barco_orientado = (1, barco[0])

        posicion_valida = posicion(tablero, d_filas, d_cols, barco_orientado, (valor, indice))
        if posicion_valida:
            sobrante = calcular_sobrante((valor, indice), barco)
            if sobrante < menor_sobrante:
                menor_sobrante = sobrante
                mejor_demanda = ("fila", indice, valor)
                mejor_posicion = posicion_valida
                mejor_orientacion = barco_orientado

    for demanda in d_cols_heap:
        valor_negado, indice = demanda
        valor = -valor_negado
        barco_orientado = (barco[0], 1)

        posicion_valida = posicion(tablero, d_filas, d_cols, barco_orientado, (valor, indice))
        if posicion_valida:
            sobrante = calcular_sobrante((valor, indice), barco)
            if sobrante < menor_sobrante:
                menor_sobrante = sobrante
                mejor_demanda = ("columna", indice, valor)
                mejor_posicion = posicion_valida
                mejor_orientacion = barco_orientado

    return mejor_demanda, mejor_posicion, mejor_orientacion

def queda_demanda(d_filas, d_cols): # O(W)
    i = 0
    demanda_cumplida = True
    tamaño_d_filas = len(d_filas)
    tamaño_d_cols = len(d_cols)

    while i < tamaño_d_filas and demanda_cumplida:
        demanda_cumplida = (d_filas[i] == 0)
        i += 1

    i = 0
    while i < tamaño_d_cols and demanda_cumplida:
        demanda_cumplida = (d_cols[i] == 0)
        i += 1

    return not demanda_cumplida

def actualizar_heap(d_heap, demandas): # O(W log(W))
    return heapificar_demandas(demandas)

def actualizar_tablero_y_demandas(tablero, d_filas_heap, d_filas, d_cols_heap, d_cols, pos_inicio, barco, indice_barco): # O(W W)

    filas_desactualizadas = []
    columnas_desactualizadas = []

    alto, ancho = barco

    for i in range(pos_inicio[0], pos_inicio[0] + alto):
        for j in range(pos_inicio[1], pos_inicio[1] + ancho):
            tablero[i][j] = indice_barco
            d_filas[i] -= 1
            d_cols[j] -= 1
            filas_desactualizadas.append(i)
            columnas_desactualizadas.append(j)

def construir_tablero(n, m): # O(W.W)
    return [[AGUA for j in range(m)] for i in range(n)]

def battleship_greedy(demandas_filas, demandas_columnas, barcos_originales): 
    tablero = construir_tablero(len(demandas_filas), len(demandas_columnas)) #O (W.W)

    d_filas = demandas_filas.copy() # O(W)
    d_cols = demandas_columnas.copy() # O(W)

    d_filas_heap = heapificar_demandas(d_filas) # O(W log(W))
    d_cols_heap = heapificar_demandas(d_cols)  # O(W log(W))
    
    barcos = sorted(list(zip(barcos_originales, range(len(barcos_originales)))), reverse=True, key=lambda b: b[0]) # O(W log(W))

    while barcos and queda_demanda(d_filas, d_cols): 
        barco = barcos.pop(0)

        mejor_demanda, mejor_posicion, mejor_orientacion = encontrar_mejor_demanda( # O(W.W.W)
            tablero, d_filas, d_cols, barco, d_filas_heap, d_cols_heap
        )

        if mejor_demanda and mejor_posicion:
            actualizar_tablero_y_demandas( # O(W W)
                tablero, d_filas_heap, d_filas, d_cols_heap, d_cols, mejor_posicion, mejor_orientacion, barco[1]
            )
            d_filas_heap = actualizar_heap(d_filas_heap, d_filas) # O(W log(W))
            d_cols_heap = actualizar_heap(d_cols_heap, d_cols) # O(W log(W))

    return tablero