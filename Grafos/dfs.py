#Recorrer desde un origen
def dfs(grafo, v, visitados, padre, orden): #O(V+E)
    visitados.agregar(v)
    for w in grafo.adyacentes(v):
        if w not in visitados:
            visitados.agregar(w)
            padre[w] = v
            orden[w] = orden[v] + 1
            dfs(grafo, w, visitados, padre, orden)

def recorrido_dfs_completo(grafo, origen):
    visitados = set()
    padres = {}
    orden ={}
    padre[origen] = None
    orden[padre] = 0
    dfs(grafo, origen, visitados, padre, orden)
    return padre, orden
#------------------------------------------------
#Recorrer todo el grafo
def dfs(grafo, v, visitados, padre, orden):
    visitados.agregar(v)
    for w in grafo.adyacentes(v):
        if w not in visitados:
            visitados.agregar(w)
            padre[w] = v
            orden[w] = orden[v] + 1
            dfs(grafo, w, visitados, padre, orden)

def recorrido_dfs_completo(grafo, origen):
    visitados = set()
    padres = {}
    orden ={}
    for v in grafo:
        if v not in visitados:               
            padre[v] = None
            orden[v] = 0
            dfs(grafo, origen, visitados, padre, orden)
    return padre, orden

