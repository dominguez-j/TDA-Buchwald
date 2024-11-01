class Grafo:
	def __init__(self, es_dirigido = False, vertices_init = []):
		self.vertices = {}
		for v in vertices_init:
			self.vertices[v] = {}
		self.es_dirigido = es_dirigido

	def __contains__(self, v):
		return v in self.vertices

	def __len__(self):
		return len(self.vertices)

	def __iter__(self):
		return iter(self.vertices)

	def agregar_vertice(self, v):
		if v in self:
			raise ValueError("Ya hay un vertice " + str(v) + " en el grafo")
		self.vertices[v] = {}

	def _validar_vertice(self, v):
		if v not in self:
			raise ValueError("No hay un vertice " + str(v) + " en el grafo")

	def _validar_vertices(self, v, w):
		self._validar_vertice(v)
		self._validar_vertice(w)

	def borrar_vertice(self, v):
		self._validar_vertice(v)
		for w in self:
			if v in self.vertices[w]:
				del self.vertices[w][v]
		del self.vertices[v]

	def agregar_arista(self, v, w, peso = 1):
		self._validar_vertices(v, w)
		if self.estan_unidos(v, w):
			raise ValueError("El vertice " + str(v) + " ya tiene como adyacente al vertice " + str(w))
		
		self.vertices[v][w] = peso
		if not self.es_dirigido:
			self.vertices[w][v] = peso

	def borrar_arista(self, v, w):
		self._validar_vertices(v, w)
		if not self.estan_unidos(v, w):
			raise ValueError("El vertice " + str(v) + " no tiene como adyacente al vertice " + str(w))

		del self.vertices[v][w]
		if not self.es_dirigido:
			del self.vertices[w][v]

	def estan_unidos(self, v, w):
		return w in self.vertices[v]

	def peso_arista(self, v, w):
		if not self.estan_unidos(v, w):
			raise ValueError("El vertice " + str(v) + " no tiene como adyacente al vertice " + str(w))
		return self.vertices[v][w]

	def obtener_vertices(self):
		return list(self.vertices.keys())

	def vertice_aleatorio(self):
		return self.obtener_vertices()[0]

	def adyacentes(self, v):
		self._validar_vertice(v)
		return list(self.vertices[v].keys())

	def __str__(self):
		cad = ""
		for v in self:
			cad += v
			for w in self.adyacentes(v):
				cad += " -> " + w 
			cad += "\n"
		return cad