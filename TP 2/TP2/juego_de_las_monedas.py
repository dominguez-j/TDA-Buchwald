# La ecuación de recurrencia es:
#
#   OPT(i, j) = {
#               max(M[i] + OPT(p(i + 1, j)), M[j] OPT(p(i, j - 1))) <-> i < j
#               M[i] <-> i == j
#               0 <-> i > j
#           }
#
# Esta definición incluye los dos casos base. Los parámetros i y j son índices
# del arreglo original de monedas M, por lo que vamos a ir considerando
# 'porciones' del arreglo según estos límites.
# La función 'p' es solo ilustrativa: actualiza los valores de (i, j) según qué
# moneda toma Mateo. Por ejemplo, si, dados (i, j), Mateo toma la última moneda,
# p(i, j) = (i, j - 1), y si toma la primera, p(i, j) = (i + 1, j). Aún así,
# por motivos prácticos, se omite su implementación explicita.

def nuevos_indices(indices, monedas): # Función p
    if monedas[indices[0]] >= monedas[indices[1]]:
        return indices[0] + 1, indices[1]
    else:
        return indices[0], indices[1] - 1

def matriz_de_optimos(monedas):
    opt = [[0] * len(monedas) for _ in range(0, len(monedas))]

    for j in range(0, len(monedas)):
        # Las diagonales son triviales
        opt[j][j] = monedas[j]
        for k in range(1, j + 1):
            # Definimos i. Con esta transformación, i es el índice inferior del arreglo de monedas,
            # y j el índice superior.
            i = j - k

            # Definimos dos nuevos pares de índices. Para eso, consideramos que
            # Sophia puede tomar la primera o última moneda, y luego vemos qué
            # decisión tomaría mateo.
            nuevo_inf_1, nuevo_sup_1 = nuevos_indices((i + 1, j), monedas)
            nuevo_inf_2, nuevo_sup_2 = nuevos_indices((i, j - 1), monedas)

            max_tomando_inf = monedas[i]
            max_tomando_sup = monedas[j]

            # Siempre que los índices no se vayan de rango, sumamos el óptimo del
            # par indicado.
            if nuevo_inf_1 <= nuevo_sup_1:
                max_tomando_inf += opt[nuevo_inf_1][nuevo_sup_1]

            if nuevo_inf_2 <= nuevo_sup_2:
                max_tomando_sup += opt[nuevo_inf_2][nuevo_sup_2]

            # Aplicamos la ecuación de recurrencia directamente.
            opt[i][j] = max(
                max_tomando_inf,
                max_tomando_sup
            )

    return opt

def reconstruir_pasos(opt, monedas):
    i, j = 0, len(monedas) - 1

    decisiones_sophia = []
    decisiones_mateo = []

    while i <= j:
        # Para reconstruir, aplicamos la ecuación de recurrencia a la inversa
        nuevo_inf_1, nuevo_sup_1 = nuevos_indices((i + 1, j), monedas)
        max_tomando_inf = monedas[i]
        if nuevo_inf_1 <= nuevo_sup_1:
            max_tomando_inf += opt[nuevo_inf_1][nuevo_sup_1]

        # Si el valor en la posición corresponde a una elección, se toma esa, si no, la otra
        if opt[i][j] == max_tomando_inf:
            decisiones_sophia.append(f"Sophia debe agarrar la primera ({monedas[i]})")
            i += 1
        else:
            decisiones_sophia.append(f"Sophia debe agarrar la ultima ({monedas[j]})")
            j -= 1

        if i <= j:
            if monedas[i] > monedas[j]:
                decisiones_mateo.append(f"Mateo agarra la primera ({monedas[i]})")
                i += 1
            else:
                decisiones_mateo.append(f"Mateo agarra la ultima ({monedas[j]})")
                j -= 1

    return decisiones_sophia, decisiones_mateo

def resultado_del_juego(monedas):
    opt = matriz_de_optimos(monedas)
    pasos = reconstruir_pasos(opt, monedas)
    return (opt, pasos)