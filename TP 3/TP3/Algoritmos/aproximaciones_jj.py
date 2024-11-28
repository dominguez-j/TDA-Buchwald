from ..Utilidades.utils_generales import AGUA

# Voy a asumir que un tablero se indexa como tablero[fila][columna]. Es decir,
# len(tablero) = cantidad de filas, len(tablero[0]) = cantidad de columnas

def maximos(arreglo): # O(W)
    maximo = arreglo[0]
    indices = []
    for i in range(len(arreglo)):
        if arreglo[i] == maximo:
            indices.append(i)
        elif arreglo[i] > maximo:
            maximo = arreglo[i]
            indices.clear()
            indices.append(i)
    return indices

def ocupada(tablero, casilla): # O(1)
    return tablero[casilla[0]][casilla[1]] != AGUA

def bloque(tablero, casilla): # O(1), el tamaño máximo del bloque es de 9 casillas
    adyacentes = []
    for i in range(casilla[0] - 1, casilla[0] + 2):
        for j in range(casilla[1] - 1, casilla[1] + 2):
            if i >= 0 and j >= 0 and i < len(tablero) and j < len(tablero[0]):
                adyacentes.append((i, j))
    return adyacentes

def adyacentes_libres(tablero, posicion, alto, ancho): # O(W)

    casillas = [(posicion[0] + i, posicion[1] + j) for i in range(alto) for j in range(ancho)]

    for casilla in casillas:
        if casilla[0] < 0 or casilla[0] >= len(tablero) or casilla[1] < 0 or casilla[1] >= len(tablero[0]):
            return False
        bloque_adyacentes = bloque(tablero, casilla)
        for celda in bloque_adyacentes:
            if ocupada(tablero, celda):
                return False

    return True

def demandas_validas(d_filas, d_cols, posicion, alto, ancho): # O(W)
    d_filas_actualizadas = {}
    d_cols_actualizadas = {}

    for i in range(posicion[0], posicion[0] + alto):
        for j in range(posicion[1], posicion[1] + ancho):

            if i not in d_filas_actualizadas:
                d_filas_actualizadas[i] = d_filas[i]
            d_filas_actualizadas[i] -= 1

            if j not in d_cols_actualizadas:
                d_cols_actualizadas[j] = d_cols[j]
            d_cols_actualizadas[j] -= 1

            if d_filas_actualizadas[i] < 0 or d_cols_actualizadas[j] < 0:
                return False

    return True

def posicion(tablero, d_filas, d_cols, barco, demanda, longitud_demandas, indice): # O(W²)
    lado_mas_largo = max(barco[0], barco[1])

    if demanda - lado_mas_largo < 0:
        return None

    # O(W²)
    for i in range(longitud_demandas - lado_mas_largo): # O(W)
        pos_inicio = (indice, i) if barco[0] == 1 else (i, indice)

        no_tiene_adyacentes = adyacentes_libres(tablero, pos_inicio, barco[0], barco[1]) # O(W)
        no_excede_demandas = demandas_validas(d_filas, d_cols, pos_inicio, barco[0], barco[1]) # O(W)
        posicion_valida = no_tiene_adyacentes and no_excede_demandas

        if posicion_valida:
            return pos_inicio

    return None

def queda_demanda(d_filas, d_cols): # O(W)
    for d in d_filas:
        if d != 0:
            return True
    for d in d_cols:
        if d != 0:
            return True

    return False

def actualizar_tablero_y_demandas(tablero, d_filas, d_cols, pos_inicio, barco, indice_barco): # O(W)

    alto, ancho = barco

    # Aunque se usa un doble for, cuando uno de ellos tiene complejidad O(W), el otro siempre toma
    # una única iteración, debido a que los barcos son de ancho 1, así que en total toman O(W)
    for i in range(pos_inicio[0], pos_inicio[0] + alto): # O(W), O(1)
        for j in range(pos_inicio[1], pos_inicio[1] + ancho): # O(1), O(W)
            tablero[i][j] = indice_barco
            d_filas[i] -= 1
            d_cols[j] -= 1

def construir_tablero(n, m):
    return [[AGUA for j in range(m)] for i in range(n)]

def intentar_colocar(tablero, d_filas, d_cols, indice_barco, barco, demandas, indice_demanda): # O(W²)

    posicion_en_fila = posicion(tablero, d_filas, d_cols, barco, demandas[indice_demanda], len(demandas), indice_demanda) # O(W²)
    if posicion_en_fila is not None:
        actualizar_tablero_y_demandas(tablero, d_filas, d_cols, posicion_en_fila, barco, indice_barco) # O(W)
        return True
    return False

def battleship_aproximacion(demandas_filas, demandas_columnas, barcos_originales): # O(W³)

    # Los siguientes serán los tamaños asociados a cada entrada:
    #   1. Una matriz es de tamaño n x m
    #   2. n es la cantidad de filas
    #   3. m es la cantidad de columnas
    #   4. b es la cantidad de barcos
    #   5. Usaremos que W = max(n, m)
    #
    #   Una consideración es que el barco de mayor tamaño que el algoritmo principal considerará es de W. Barcos de
    #   mayor tamaño nunca alcanzarán el algoritmo principal.

    tablero = construir_tablero(len(demandas_filas), len(demandas_columnas)) # O(W²)

    d_filas = demandas_filas.copy()
    d_cols = demandas_columnas.copy()

    barcos = sorted(list(zip(barcos_originales, range(len(barcos_originales)))), reverse = True, key = lambda b: b[0]) # O(b · log(b))

    i = 0 # Para iterar sobre los barcos

    # El bucle termina al suplir con todas las demandas de filas o columnas, o al haber revisado todos los barcos
    # O(W² · b)
    while i < len(barcos) and queda_demanda(d_filas, d_cols): # O(b)
        indice_barco = barcos[i][1]

        # Ubico todos los máximos. Esto es por si hay varias filas/columnas con la misma demanda
        maximos_filas = maximos(d_filas) # O(W)
        maximos_cols = maximos(d_cols) # O(W)

        primer_maximo_filas = d_filas[maximos_filas[0]]
        primer_maximo_cols = d_cols[maximos_cols[0]]

        # Algunas 'podas'

        # O(1)
        if barcos[i][0] > primer_maximo_filas and barcos[i][0] > primer_maximo_cols:
            i += 1
            continue

        # O(1)
        if barcos[i][0] > max(len(tablero), len(tablero[0])):
            i += 1
            continue

        barco_h = (1, barcos[i][0]) # Barco dispuesto horizontalmente, en una fila
        barco_v = (barcos[i][0], 1) # Barco dispuesto verticalmente, en una columna

        j = 0
        colocado = False

        if primer_maximo_filas >= primer_maximo_cols:
            # O(W² · b)
            while j < len(maximos_filas) and not colocado: # O(b)
                colocado = intentar_colocar( # O(W²)
                    tablero,
                    d_filas,
                    d_cols,
                    indice_barco,
                    barco_h,
                    d_filas,
                    maximos_filas[j]
                )
                j += 1
            if not colocado and primer_maximo_filas == primer_maximo_cols:
                while j < len(maximos_cols) and not colocado: # O(W)
                    colocado = intentar_colocar( # O(W²)
                        tablero,
                        d_filas,
                        d_cols,
                        indice_barco,
                        barco_v,
                        d_cols,
                        maximos_cols[j]
                    )
                    j += 1
        else:
            # O(W² · b)
            while j < len(maximos_cols) and not colocado: # O(W)
                colocado = intentar_colocar( # O(W²)
                    tablero,
                    d_filas,
                    d_cols,
                    indice_barco,
                    barco_v,
                    d_cols,
                    maximos_cols[j]
                )
                j += 1

        i += 1

    return tablero