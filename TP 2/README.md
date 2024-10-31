## Teoría de Algoritmos - Buchwald - Trabajo Práctico N° 2

## Integrantes:
- Dominguez, Jonathan - 110057 - jgdominguez@fi.uba.ar
- Godoy Serrano, Mateo - 110912 - mvserrano@fi.uba.ar
- Pato Ibáñez, Manuel - 110640 - mpato@fi.uba.ar

## Consigna
****1.****  Hacer un análisis del problema, plantear la ecuación de recurrencia correspondiente y proponer un algoritmo por programación dinámica que obtenga la solución óptima al problema planteado: Dada la secuencia de monedas $m_1, m_2, ..., m_n$, sabiendo que Sophia empieza el juego y que Mateo siempre elegirá la moneda más grande para sí entre la primera y la última moneda en sus respectivos turnos, definir qué monedas debe elegir Sophia para asegurarse obtener el __máximo valor acumulado posible__. Esto no necesariamente le asegurará a Sophia ganar, ya que puede ser que esto no sea obtenible, dado por cómo juega Mateo. Por ejemplo, para [1, 10, 5], no importa lo que haga Sophia, Mateo ganará.

****2.**** Demostrar que la ecuación de recurrencia planteada en el punto anterior en efecto nos lleva a obtener el __máximo valor acumulado posible__.

****3.**** Escribir el algoritmo planteado. Describir y justificar la complejidad de dicho algoritmo. Analizar si (y cómo) afecta a los tiempos del algoritmo planteado la variabilidad de los valores de las monedas.

****4.**** Realizar ejemplos de ejecución para encontrar soluciones y corroborar lo encontrado. Adicionalmente, el curso proveerá con algunos casos particulares que deben cumplirse su optimalidad también.

****5.**** Hacer mediciones de tiempos para corroborar la complejidad teórica indicada. Agregar los casos de prueba necesarios para dicha corroboración. Esta corroboración empírica debe realizarse confeccionando gráficos correspondientes, y utilizando la técnica de cuadrados mínimos.

****6.**** Agregar cualquier conclusión que les parezca relevante.

## Cómo ejecutarlo

Si bien quedaron registradas las implementaciones de los tests, del álgebra y de la generación de gráficos, el script `main.py` es
el principal. Para ejecutarlo, se debe llamar por consola a `python main.py`. No es necesario contar con la solución esperada
para ejecutar los tests, pero sí seguir un formato estricto de escritura, visible en los ejemplos de la carpeta `Ejemplos`.

Para información sobre los tests, consultar la carpeta `Tests añadidos`
