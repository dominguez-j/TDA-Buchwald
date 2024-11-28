AGUA = '-'
ORIENTACIONES = [(0, 1), (1, 0)]
ADYACENTES = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]

def operar_sobre_datos(datos):
    valores = [[], [], []]
    grupo_actual = 0

    for dato in datos:
        if dato == ' ':
            grupo_actual += 1
            continue
        valores[grupo_actual].append(dato)
    return valores

def formatear_datos_en_lista(datos, separador):
    return separador.join(list(filter(lambda dato: dato != '', datos)))

def formatear_valor(valor):
    return str(valor)

# Utils para el problema de Batalla Naval

def organizar_resultados(resultado, parametros):
    tablero = resultado
    demanda_filas, demanda_columnas, barcos = parametros
    demanda_total = sum(demanda_filas) + sum(demanda_columnas)
    demanda_cumplida = sum(
        2 for fila in tablero for celda in fila if celda != AGUA)

    posiciones_dict = {idx: [] for idx in range(len(barcos))}

    for fila in range(len(tablero)):
        for columna in range(len(tablero[0])):
            celda = tablero[fila][columna]
            if celda != AGUA:
                posiciones_dict[celda].append((fila, columna))

    posiciones = []
    for idx in range(len(barcos)):
        if posiciones_dict[idx]:
            pos_str = ' - '.join(f'({fila}, {columna})' for fila, columna in posiciones_dict[idx])
            posiciones.append(f'{idx}: {pos_str}')
        else:
            posiciones.append(f'{idx}: None')
            
    tablero_str = ' '
    for fila in resultado:
       tablero_str += f'\n{" ".join(f"{str(num):>2}" for num in fila)}'
    # Construir el resultado como una cadena con saltos de línea
    texto = (
        tablero_str,
        'Posiciones:',
        *posiciones,
        f'Demanda cumplida: {demanda_cumplida}',
        f'Demanda total: {demanda_total}',
    )

    # Unir la tupla en una sola cadena con saltos de línea
    return '\n'.join(texto)

def organizar_resultados_pl(resultado, parametros):
    demanda_filas, demanda_columnas, _ = parametros

    tablero = [[AGUA for j in range(len(demanda_columnas))] for i in range(len(demanda_filas))]

    for variable_pulp in resultado:
        variable = str(variable_pulp).split('_')[1:-1]
        tablero[int(variable[0])][int(variable[1])] = int(variable[2])

    return organizar_resultados(tablero, parametros)