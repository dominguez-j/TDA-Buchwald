from ..Utilidades.utils_generales import AGUA, ORIENTACIONES, ADYACENTES

def verificar_solucion(tablero, demanda_filas, demanda_columnas, barcos): # O(n*m + b)
    """
    Verifica si la solución es correcta.
    - No hay superposiciones de barcos.
    - No hay barcos adyacentes (ni horizontal, vertical, ni diagonalmente).
    - Se cumple con la demanda de cada fila y columna.
    - Que estén todos los barcos colocados y respeten sus tamaños.
    """
    filas = len(tablero)
    columnas = len(tablero[0])
    
    if not verificar_adyacencias(tablero, filas, columnas): # O(n*m)
        return False

    if not verificar_demanda(tablero, demanda_filas, demanda_columnas): # O(n*m)
        return False

    if not verificar_barcos(tablero, filas, columnas, barcos): # O(n*m + b)
        return False
    
    return True

def verificar_adyacencias(tablero, filas, columnas):
    # Verificar que no hay barcos adyacentes
    for f in range(filas):
        for c in range(columnas):
            if tablero[f][c] != AGUA:
                for df, dc in ADYACENTES:  # Revisar todas las posiciones adyacentes
                    ady_f, ady_c = f + df, c + dc
                    if (0 <= ady_f < filas and 0 <= ady_c < columnas and tablero[ady_f][ady_c] != AGUA):
                        if tablero[f][c] != tablero[ady_f][ady_c]:
                            return False
    return True

def verificar_demanda(tablero, demanda_filas, demanda_columnas):
    
    # Verificar que las demandas de filas se cumplen
    for i, demanda in enumerate(demanda_filas):
        if sum(1 for celda in tablero[i] if celda != AGUA) != demanda:
            return False

    # Verificar que las demandas de columnas se cumplen
    for j, demanda in enumerate(demanda_columnas):
        if sum(1 for fila in tablero if fila[j] != AGUA) != demanda:
            return False
        
    return True

def verificar_barcos(tablero, filas, columnas, barcos):
    # Identificar los barcos presentes en el tablero
    barcos_encontrados = {}
    visitado = [[False] * columnas for _ in range(filas)]
    
    def dfs(f, c, barco_id, direcciones):
        # Realiza una DFS para encontrar un barco completo.
        visitado[f][c] = True
        tamaño = 1
        for df, dc in direcciones:
            nf, nc = f + df, c + dc
            if 0 <= nf < filas and 0 <= nc < columnas and not visitado[nf][nc] and tablero[nf][nc] == barco_id:
                tamaño += dfs(nf, nc, barco_id, direcciones)
        return tamaño
    
    for f in range(filas):
        for c in range(columnas):
            if tablero[f][c] != AGUA and not visitado[f][c]:
                barco_id = tablero[f][c]
                # Verificar si el barco es horizontal o vertical
                tamaño_barco = dfs(f, c, barco_id, ORIENTACIONES)
                if barco_id in barcos_encontrados:
                    return False  # Barco duplicado
                barcos_encontrados[barco_id] = tamaño_barco

    # Verificar que todos los barcos están presentes y tienen el tamaño correcto
    barcos_esperados = {idx: barcos[idx] for idx in range(len(barcos))}
    if barcos_encontrados != barcos_esperados:
        return False  # Faltan barcos, hay barcos de más o tamaños incorrectos