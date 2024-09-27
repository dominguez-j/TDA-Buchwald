## Teoría de Algoritmos - Buchwald - Trabajo Práctico N° 1

## Integrantes:
- Dominguez, Jonathan - 110057 - jgdominguez@fi.uba.ar
- Godoy Serrano, Mateo - 110912 - mvserrano@fi.uba.ar
- Pato Ibáñez, Manuel - 110640 - mpato@fi.uba.ar

## Consigna
****1.****  Hacer un análisis del problema, y proponer un algoritmo greedy que obtenga la solución óptima al problema planteado: 
Dados los n valores de todas las monedas, indicar qué monedas debe ir eligiendo Sophia para si misma y para Mateo, de tal forma que se asegure de ganar siempre. Considerar que Sophia siempre comienza (para sí misma).

****2.**** Demostrar que el algoritmo planteado obtiene siempre la solución óptima (desestimando el caso de una cantidad par de monedas de mismo valor, en cuyo caso siempre sería empate más allá de la estrategia de Sophia).

****3.**** Escribir el algoritmo planteado. Describir y justificar la complejidad de dicho algoritmo. Analizar si (y cómo) afecta la variabilidad de los valores de las diferentes monedas a los tiempos del algoritmo planteado.

****4.**** Analizar si (y cómo) afecta la variabilidad de los valores de las diferentes monedas a la optimalidad del algoritmo planteado.

****5.**** Realizar ejemplos de ejecución para encontrar soluciones y corroborar lo encontrado. Adicionalmente, el curso proveerá con algunos casos particulares que deben cumplirse su optimalidad también.

****6.**** Hacer mediciones de tiempos para corroborar la complejidad teórica indicada. Agregar los casos de prueba necesarios para dicha corroboración. Esta corroboración empírica debe realizarse confeccionando gráficos correspondientes, y utilizando la técnica de cuadrados mínimos.

****7.**** Agregar cualquier conclusión que les parezca relevante.

## Cómo ejecutarlo

Si bien quedaron registradas las implementaciones de los tests, del álgebra y de la generación de gráficos, el script `main.py` es
el principal. Para ejecutarlo, se debe llamar por consola a `python main.py`. No es necesario contar con la solución esperada
para ejecutar los tests, pero sí seguir un formato estricto de escritura, visible en los ejemplos de la carpeta `Ejemplos`.

Se pueden ejecutar las pruebas de la cátedra con `python -m TP1.Tests.test_catedra`, y nuestras pruebas locales con
`python -m TP1.Tests.test_locales`.