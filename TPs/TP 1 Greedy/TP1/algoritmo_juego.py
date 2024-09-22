def juego_de_la_moneda(monedas):
    arr_sophia, arr_mateo, pasos = [], [], []
    i, j = [0], [len(monedas) -1]
    es_turno_de_sophia = True

    while i[0] <= j[0]:     
        if es_turno_de_sophia:
            elige_sophia(i, j, arr_sophia, monedas, pasos)
        else:
            elige_mateo(i, j, arr_mateo, monedas, pasos)
        es_turno_de_sophia = not es_turno_de_sophia

    return (arr_sophia, arr_mateo, pasos)

def elige_sophia(i, j, arr_sophia, monedas, pasos):
    if monedas[i[0]] >= monedas[j[0]]:
        arr_sophia.append(monedas[i[0]])
        pasos.append('Primera moneda para Sophia')
        i[0] += 1
    else:
        pasos.append('Última moneda para Sophia')
        arr_sophia.append(monedas[j[0]])
        j[0] -= 1

def elige_mateo(i, j, arr_mateo, monedas, pasos):
    if monedas[i[0]] <= monedas[j[0]]:
        arr_mateo.append(monedas[i[0]])
        pasos.append('Primera moneda para Mateo')
        i[0] += 1
    else:
        arr_mateo.append(monedas[j[0]])
        pasos.append('Última moneda para Mateo')
        j[0] -= 1