def orden_topologico_BFS(grafo): #O(V+E)
    grados = {}
    for v in grafo:
        grados[v] = 0
    for v in grafo:
        for w in grafo.adyacentes(v):
            grados[w] += 1
    q = cola()
    for v in grafo:
        if grados[v] == 0:
            q.encolar(v)
    resul = []
    
    while not q.esta_vacia(): 
        v = q.desencolar() 
        resul.append(v)
        for w in grafo. adyacentes (v): 
            grados [w] -= 1
            if grados [v] == 0: 
                q.encolar (w)
       if len(resul) == len(grafo):
           return resul
        else:
            return None # El grafo tiene algun ciclo
#----------------------------------
def orden_topologico_DFS(grafo): #O(V+E)
    visitados = set()
    pila = Pila()
    for v in grafo:
        if v not in visitados:
            orden_topologico_rec(grafo, v, pila, visitados)
    return pila_a_lista(pila)
    
def orden_topologico_rec(grafo, v, pila, visitados): 
    visitados.agregar(v)
    for w in grafo.adyacentes(v): 
        if w not in visitados:
            orden_topologico(grafo, v, pila, visitados)
    pila.apilar(v)