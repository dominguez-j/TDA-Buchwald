from .. utils import leer_datos
from . funciones_auxiliares_mediciones import *
from . hallar_aproximacion import *

import matplotlib.pyplot as plt
import numpy as np

mediciones = leer_datos(ruta_absoluta_resultados, lectura_de_mediciones)
funcion = funcion_aproximadora(complejidad, mediciones)
errores_por_medicion, error_cuadratico_total = errores(funcion, mediciones)

tamaños_de_entrada = np.array([medicion[0] for medicion in mediciones])
tiempos_empiricos = np.array([medicion[1] for medicion in mediciones])

aproximaciones = np.array([funcion(tamaño) for tamaño in tamaños_de_entrada])

plt.figure()
plt.grid(True)
plt.title('Tiempo de ejecución real del algoritmo')
plt.xlabel('Tamaño de la muestra')
plt.ylabel('Tiempo de ejecución (ms)')
plt.plot(tamaños_de_entrada, tiempos_empiricos, color = 'blue')
plt.savefig(ruta_absoluta_grafico_medicion_real)

plt.figure()
plt.grid(True)
plt.title('Comparación entre la medición real y el ajuste')
plt.xlabel('Tamaño de la muestra')
plt.ylabel('Tiempo de ejecución (ms)')
plt.plot(tamaños_de_entrada, tiempos_empiricos, color = 'blue', label="Medición")
plt.plot(tamaños_de_entrada, aproximaciones, color = 'red', linestyle='--', label="Ajuste")
plt.legend()
plt.savefig(ruta_absoluta_grafico_comparacion)

plt.figure()
plt.grid(True)
plt.title('Error del ajuste')
plt.xlabel('Tamaño de la muestra')
plt.ylabel('Error (ms)')
plt.plot(tamaños_de_entrada, errores_por_medicion, color = 'blue')
plt.text(3000, max(errores_por_medicion) - min(errores_por_medicion),"ECT = " + str(error_cuadratico_total), fontsize=10, color='black')
plt.savefig(ruta_absoluta_grafico_errores)
