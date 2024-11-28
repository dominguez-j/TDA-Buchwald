from ..Utilidades.utils_generales import AGUA, ORIENTACIONES, ADYACENTES

def copiar_tablero(tablero):
    return [fila[:] for fila in tablero]

def actualizar_demanda_incumplida(estado):
    estado["incumplimiento"] = sum(estado["demanda_filas"]) + sum(estado["demanda_columnas"])

def poner_barco(tablero, fila, columna, orientacion, barco, idx_b):
    for i in range(barco):
        tablero[fila + i * orientacion[1]][columna + i * orientacion[0]] = idx_b

def sacar_barco(tablero, fila, columna, orientacion, barco):
    for i in range(barco):
        tablero[fila + i * orientacion[1]][columna + i * orientacion[0]] = AGUA

def actualizar_demandas(fila, columna, estado, orientacion, barco, valor):
    for i in range(barco):
        f = fila + i * orientacion[1]
        c = columna + i * orientacion[0]
        estado["demanda_filas"][f] += valor
        estado["demanda_columnas"][c] += valor

def battleship(demanda_filas, demanda_columnas, barcos):
    estado = {"tablero": [[AGUA for _ in range(len(demanda_columnas))] for _ in range(len(demanda_filas))],
                    "demanda_filas": demanda_filas[:], "demanda_columnas": demanda_columnas[:],
                    "incumplimiento": float("inf")}
    mejor_tablero = {"tablero": None, "incumplimiento": float("inf")}
    barcos_ord = sorted(barcos, reverse=True)
    ultima_posicion = {"fila": 0, "columna": 0, "tamaño": 0}
    battleship_bt(estado, barcos_ord, 0, mejor_tablero, ultima_posicion)
    return mejor_tablero["tablero"]

def battleship_bt(estado, barcos, idx_b, mejor_tablero, ultima_posicion):
    actualizar_demanda_incumplida(estado)
     
    # Caso base
    if idx_b >= len(barcos): 
        if estado["incumplimiento"] < mejor_tablero["incumplimiento"]:
            mejor_tablero["tablero"] = copiar_tablero(estado["tablero"])
            mejor_tablero["incumplimiento"] = estado["incumplimiento"]   
        return
    
    barco = barcos[idx_b]  
    # Poda: si no hay espacio suficiente para este barco
    if barco > max(max(estado["demanda_filas"]), max(estado["demanda_columnas"])):
        battleship_bt(estado, barcos, idx_b + 1, mejor_tablero, ultima_posicion) 
        return

    # Poda: si la solución actual ya es peor que la mejor encontrada
    demanda_restante = 2 * sum(barcos[idx_b:])
    if estado["incumplimiento"] - demanda_restante >= mejor_tablero["incumplimiento"]:
        return
    
    # Determinar desde dónde iniciar la búsqueda
    inicio_fila, inicio_columna = 0, 0
    if ultima_posicion["tamaño"] == barco:
        inicio_fila, inicio_columna = ultima_posicion["fila"], ultima_posicion["columna"]      
    
    for fila in range(inicio_fila, len(estado["tablero"])):
        if estado["demanda_filas"][fila] == 0: continue
        for columna in range(inicio_columna if fila == inicio_fila else 0, len(estado["tablero"][0])):
            if estado["demanda_columnas"][columna] == 0: continue
            if estado["tablero"][fila][columna] != AGUA: continue
            if estado["demanda_filas"][fila] < barco and estado["demanda_columnas"][columna] < barco: continue
            for orientacion in ORIENTACIONES:   
                if es_compatible(estado, fila, columna, orientacion, barco):
                    poner_barco(estado["tablero"], fila, columna, orientacion, barco, idx_b)
                    actualizar_demandas(fila, columna, estado, orientacion, barco, -1)
                    
                    if orientacion == (0, 1):  # Horizontal
                        ultima_posicion["fila"] = fila
                        ultima_posicion["columna"] = columna + barco
                    elif orientacion == (1, 0):  # Vertical
                        ultima_posicion["fila"] = fila + barco
                        ultima_posicion["columna"] = columna
                    
                    ultima_posicion["tamaño"] = barco
                    battleship_bt(estado, barcos, idx_b + 1, mejor_tablero, ultima_posicion)

                    actualizar_demandas(fila, columna, estado, orientacion, barco, 1)
                    sacar_barco(estado["tablero"], fila, columna, orientacion, barco)
                    
    # Reinicio de última posición si se pasa al siguiente barco
    ultima_posicion["fila"], ultima_posicion["columna"], ultima_posicion["tamaño"] = 0, 0, 0
    battleship_bt(estado, barcos, idx_b + 1, mejor_tablero, ultima_posicion)   

def es_compatible(estado, fila, columna, orientacion, barco):
    filas, columnas = len(estado["tablero"]), len(estado["tablero"][0])
    
    if not puede_entrar(fila, columna, estado["demanda_filas"], estado["demanda_columnas"], orientacion, barco):
        return False
    if not no_excede_demandas(fila, columna, orientacion, barco, estado["demanda_filas"], estado["demanda_columnas"]):
        return False
    if not se_puede_colocar(fila, columna, filas, columnas, orientacion, barco, estado["tablero"]):
        return False
    
    return True

def puede_entrar(fila, columna, demanda_filas, demanda_columnas, orientacion, barco):
    if orientacion == (1, 0):
        if demanda_filas[fila] < barco: # Si la demanda de la fila es menor al tamaño del barco
            return False
        if columna + (barco - 1) > len(demanda_columnas): # Si el barco se sale del tablero
            return False 
    elif orientacion == (0, 1): 
        if demanda_columnas[columna] < barco: # Si la demanda de la columna es menor al tamaño del barco
            return False
        if fila + (barco - 1) > len(demanda_filas): # Si el barco se sale del tablero
            return False
    return True 

def no_excede_demandas(fila, columna, orientacion, barco, demanda_filas, demanda_columnas):
    if orientacion == (1, 0):  # Horizontal
        # Verificar cada columna individualmente
        for i in range(barco):
            c = columna + i
            if c < len(demanda_columnas) and demanda_columnas[c] < 1:
                return False
    elif orientacion == (0, 1):  # Vertical
        # Verificar cada fila individualmente
        for i in range(barco):
            f = fila + i
            if f < len(demanda_filas) and demanda_filas[f] < 1:
                return False
    return True

def se_puede_colocar(fila, columna, filas, columnas, orientacion, barco, tablero):     
    for i in range(barco):
        f = fila + i * orientacion[1]
        c = columna + i * orientacion[0]
        
        # Verificar si la posición está dentro del tablero o si está libre
        if not (0 <= f < filas and 0 <= c < columnas) or tablero[f][c] != AGUA:
            return False
        
        # Verificar adyacentes
        for df, dc in ADYACENTES:
            ady_f, ady_c = f + df, c + dc
            if (0 <= ady_f < filas and 0 <= ady_c < columnas and tablero[ady_f][ady_c] != AGUA):
                return False
    return True