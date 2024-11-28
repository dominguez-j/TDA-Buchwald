## Teoría de Algoritmos - Buchwald - Trabajo Práctico N° 3

## Integrantes:
- Dominguez, Jonathan - 110057 - jgdominguez@fi.uba.ar
- Godoy Serrano, Mateo - 110912 - mvserrano@fi.uba.ar
- Pato Ibáñez, Manuel - 110640 - mpato@fi.uba.ar

## Consigna
****1.**** Demostrar que el Problema de la Batalla Naval se encuentra en NP.

****2.**** Demostrar que el Problema de la Batalla Naval es, en efecto, un problema NP-Completo. Si se hace una reducción involucrando un problema no visto en clase, agregar una (al menos resumida) demostración que dicho problema es NP-Completo.

****3.**** Escribir un algoritmo que, por backtracking, obtenga la solución óptima al problema (valga la redundancia) en la versión de optimización: Dado un tablero de $n \times m$ casilleros, y una lista de $k$ barcos (donde el barco $i$ tiene $b_i$ de largo) una lista de las demandas de las $n$ filas y una lista de las $m$ demandas de las columnas, dar la asignación de posiciones de los barcos de tal forma que se reduzca al mínimo la cantidad de demanda incumplida. Pueden no utilizarse todos los barcos. Si simplemente no se cumple que una columna que debería tener 3 casilleros ocupados tiene 1, entonces contará como 2 de demanda incumplida. Por el contrario, no está permitido exceder la cantidad demandada. Generar sets de datos para corroborar su correctitud, así como tomar mediciones de tiempos.

****4.**** Escribir un modelo de programación lineal que resuelva el problema de forma óptima. Ejecutarlo para los mismos sets de datos para corroborar su correctitud. Tomar mediciones de tiempos y compararlas con las del algoritmo que implementa Backtracking.

****5.**** John Jellicoe (almirante de la Royal Navy durante la batalla de Jutlandia) nos propone el siguiente algoritmo de aproximación: Ir a fila/columna de mayor demanda, y ubicar el barco de mayor longitud en dicha fila/columna en algún lugar válido. Si el barco de mayor longitud es más largo que dicha demanda, simplemente saltearlo y seguir con el siguiente. Volver a aplicar hasta que no queden más barcos o no haya más demandas a cumplir. <br>
Este algoritmo sirve como una aproximación para resolver el problema de La Batalla Naval. Implementar dicho algoritmo, analizar su complejidad y analizar cuán buena aproximación es. Para esto, considerar lo siguiente: Sea $I$ una instancia cualquiera del problema de La Batalla Naval, y $z(I)$ una solución óptima para dicha instancia, y sea $A(I)$ la solución aproximada, se define $\frac{A(I)}{z(I)} \leq r(A)$ para todas las instancias posibles. Calcular $r(A)$ para el algoritmo dado, demostrando que la cota está bien calculada. Realizar mediciones utilizando el algoritmo exacto y la aproximación, con el objetivo de verificar dicha relación. Realizar también mediciones que contemplen volúmenes de datos ya inmanejables para el algoritmo exacto, a fin de corroborar empíricamente la cota calculada anteriormente.	

****6.**** **Opcional**: Implementar alguna otra aproximación (o algoritmo greedy) que les parezca de interés. Comparar sus resultados con los dados por la aproximación del punto anterior. Indicar y justificar su complejidad. No es obligatorio hacer este punto para aprobar el trabajo práctico (pero si resta puntos no hacerlo).

****7.**** Agregar cualquier conclusión que parezca relevante.

## Cómo ejecutarlo

Para correr test a eleccion use `main.py`. Para ejecutarlo, se debe llamar por consola a `python main.py`. No es necesario contar con la solución esperada para ejecutar los tests, pero sí seguir un formato estricto de escritura, visible en los ejemplos de la carpeta `Ejemplos`.

Para correr todos los test de la cátedra junto a todos los algoritmos correr `python -m TP3.Tests.tests_catedra`
