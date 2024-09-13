import random

class Grafo:
    def __init__(self, es_dirigido, vertices = None):
        """Crea el grafo con sus respectivos vertices, aclarando si es dirigido o no"""
        self.es_dirigido = es_dirigido
        self.vertices = {}
        if vertices is None:
            return
        else:
            for v in vertices:
                self.agregar_vertice(v)

    def agregar_vertice(self, v):
        """
        Agrega el vertice v al grafo, en caso de que ya exista este vertice, no hace nada
        """
        if not v in self.vertices:
            self.vertices[v] = {}

    def borrar_vertice(self, v):
        """
        Borra el vertice v del grafo, en caso de que el vertice no exista en el grafo, tira error
        """
        if not v in self.vertices:
            raise AssertionError("El vertice no pertenece al grafo")

        if v in self.vertices:
            self.vertices.pop(v)

        for _, dato in self.vertices:
            if v in dato:
                dato.pop(v)

    def agregar_arista(self, v, w, peso = 1):
        """
        Agrega una arista con su respectivo peso entre los vertices v y w del grafo, en caso de que 
        alguno de los vertices no pertenezca al grafo, tira error
        """
        if v not in self.vertices and not w in self.vertices:
            raise AssertionError("Algun vertice (o los dos) no pertenecen al grafo")
        
        dato_v = self.vertices[v]
        dato_v[w] = peso
        if not self.es_dirigido:
            dato_w = self.vertices[w]
            dato_w[v] = peso

    def borrar_arista(self, v, w):
        """
        Borra la arista que haya en los vertices v y w, en caso de que alguno de los vertices no pertenezca al grafo, tira error
        """
        if not v in self.vertices and not w in self.vertices:
            raise AssertionError("Algun vertice (o los dos) no pertenecen al grafo")
        
        self.vertices[v].pop(w)
        if not self.es_dirigido:
            self.vertices[w].pop(v)

    def estan_unidos(self, v, w):
        """
        Verifica si el vertice v esta unido a w, en caso de que alguno de los vertices no pertenezca al grafo, tira error
        """
        if not v in self.vertices and not w in self.vertices:
            raise AssertionError("Algun vertice (o los dos) no pertenecen al grafo")
        
        if v in self.vertices[w]:# if w in self.vertices[v]
            return True
        else:
            return False

    def peso_arista(self, v, w):
        """
        Devuelve el peso de la arista que une los vertices v y w, en caso de que alguno de los vertices no pertenezca al grafo, tira error
        """
        if not v in self.vertices and not w in self.vertices:
            raise AssertionError("Algun vertice (o los dos) no pertenecen al grafo")
        dato_v = self.vertices[v]
        return float(dato_v[w])
       
    def obtener_vertices(self):
        """
        Devuelve una lista con todos los vertices pertenecientes al grafo
        """
        vertices = []
        for v in self.vertices:
            vertices.append(v)
        return vertices
    
    def adyacentes(self, v):
        """
        Devuelve todos los vertices adyacentes a v en una lista, en caso de que el vertice no pertenezca al grafo, tira error
        """
        if not v in self.vertices:
            raise AssertionError("Algun vertice (o los dos) no pertenecen al grafo")
        vertices_adyacentes = []
        for w in self.vertices[v]:
            vertices_adyacentes.append(w)
        return vertices_adyacentes
    
    def vertice_aleatorio(self):
        """
        Devuelve un vertice perteneciente al grafo aleatoriamente, en caso de que no haya vertices en el grafo, tira error
        """
        if len(self.vertices) == 0:
            raise AssertionError("El grafo no tiene vertices")
        vertices = self.obtener_vertices()
        return vertices[random.randint(0, len(self.vertices))]