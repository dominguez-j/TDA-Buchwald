def enlistar_valores(linea):
    return [int(elemento) for elemento in linea.strip().split(';')]

def formatear_datos_en_lista(datos, separador):
    return separador.join(list(filter(lambda dato: dato != '', datos)))

def formatear_valor(valor):
    return str(valor)

def organizar_resultado_test(resultado, monedas):
    opt = resultado[0]
    pasos = resultado[1]
    if len(pasos[0]) != len(pasos[1]):
        pasos[1].append('')

    # Usando que opt[0][-1] es el valor acumulado de las monedas de Sophia,
    # sum(monedas) - opt[0][-1] es el valor acumulado de las de Mateo.
    # También, usamos tuple comprehension para intercalar los pasos entre
    # Sophia y Mateo.
    resultado = (
        tuple(paso for par_de_pasos in zip(pasos[0], pasos[1]) for paso in par_de_pasos),
        f'Ganancia Sophia: {opt[0][-1]}',
        f'Ganancia Mateo: {sum(monedas) - opt[0][-1]}'
    )
    return resultado

FUNCIONES_DE_FORMATEO = (lambda dato: formatear_datos_en_lista(dato, '; '), formatear_valor, formatear_valor)
