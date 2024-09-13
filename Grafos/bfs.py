def bfs(grafo, origen): #O(V+E)
    visitador = set()
    padres = {}
    orden = {}
    q = Cola()
    visitados.agregar(origen)
    padres[origen] = None
    orden[origen]= 0
    q.encolar(origen)
    while !q.esta_vacia(): #corre V veces
        v = q.desencolar()
        for w in grafo.adyacentes(v):
            if w not in visitados:
                visitados.agregar(w)
                padre[w] = v
                orden[w] = orden[v] + 1
                q.encolar(w)
    return padre, orden
#---------------------------------
def camino_minimo_bfs(grafo, origen):
    """
    Aplica bfs desde origen, devuelve diccionario de padres y distancias
    """
    distancia, padre, visitado = {}, {}, {}
    for v in grafo.obtener_vertices():
        distancia[v] = inf
    distancia[origen] = 0
    padre[origen] = None
    visitado[origen] = True
    q = Cola()
    q.encolar(origen)
    while not q.esta_vacia():
        v = q.desencolar()
        for w in grafo.adyacentes(v):
            if (w not in visitado):
                distancia[w] = distancia[v] + 1
                padre[w] = v
                visitado[w] = True
                q.encolar(w)
    return padre, distancia