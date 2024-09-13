def camino_minimo(grafo, origen): #O(E LOG(V)) o O(V LOG(V))
    dist ={}
    padre = { }
    for v in grafo:
        distancia[v] = infinito
    dist[origen] = 0
    padre[origen] = None
    q = heap_crear()
    q.encolar(origen, 0)
    while not q.esta_vacia():
        v = q. desencolar()
        for w in grafo.adyacentes(v):
            if dist[v] + grafo.peso_union(v,w) < dist[w]:
                dist[w] = dist[v] + grafo.peso_union(v,w)
                padre[w] = v
                q.encolar(w, dist[w])
    return padre, distancia