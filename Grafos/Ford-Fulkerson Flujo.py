def flujo(grafo, s, t):
	flujo = {}
	for v in grafo:
		for w in grafo.adyacentes(v):
			flujo[(v, w)] = 0
			
	grafo_residual = copiar(grafo)
	
	while (camino = obtener_camino(grafo_residual, s, t)) is not None:
		capacidad_residual_camino = min_peso(grafo_residual, camino)
		for i in range(1, len(camino)):
			if grafo.hay_arista(camino[i-1], camino[i]):
				flujo[(camino[i-1], camino[i])] += capacidad_residual_camino
			else:
				flujo[(camino[i], camino[i-1])] -= capacidad_residual_camino
			actualizar_grafo_residual(grafo_residual, camino[i-1], camino[i], capacidad_residual_camino)

	return flujo

def actualizar_grafo_residual(grafo_residual, u, v, valor):
	peso_anterior = grafo_residual.peso(u, v)
	if peso_anterior == valor:
		grafo_residual.remover_arista(u, v)
	else:
		grafo_residual.cambiar_peso(u, v, peso_anterior - valor)
	if not grafo_residual.hay_arista(v, u):
		grafo_residual.agregar_arista(v, u, valor)
	else:
		grafo_residual.cambiar_peso(v, u, grafo_residual.peso(v, u) + valor)