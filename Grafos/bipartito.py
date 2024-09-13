from collections import deque
def es_bipartito(grafo):
    colores = {}
    for v in grafo.vertices():
        if v not in colores:
            if not es_coloreable(grafo, v, colores):
                return False
    return True

def es_coloreable(grafo, vertice_inicial, colores):
    cola = deque()
    cola.append(vertice_inicial)
    colores[vertice_inicial] = 0
    
    while not len(cola) == 0:
        v = cola.pop()
        for w in grafo.adyacentes(v):
            if w  in colores:
               if colores[w] == colores[v]: return False
            else:
                colores[w] = 1 - colores[v]
                cola.append(w)
    return True