## Teoría de Algoritmos - Buchwald - Trabajo Práctico N° 2

### Consideraciones adicionales sobre el formato de los tests

Si se desea correr tests personalizados, se recomienda el uso de esta carpeta para mayor prolijidad.

Los tests evalúan el resultado del algoritmo principal de este TP dado un arreglo de monedas de entrada.
Para proporcionar dicho arreglo, se debe proveer un archivo de la forma `*.txt`. El formato que debe seguir
el archivo es el siguiente:

```python
# Las líneas que comiencen con un caracter '#' serán ignoradas. Puede usarse para hacer comentarios.
valor_1;valor_2;...;valor_n
```

El resultado de este test se verá reflejado en un archivo en la carpeta `Resultados` (esto es, independientemente de
si el test original se encontraba en la carpeta recomendada), con un nombre de la forma `*_resultado.txt`, cuyo
formato será el siguiente:

```
*.txt
Sophia debe agarrar la {primera/ultima} ({valor}); Mateo agarra la {primera/ultima} ({valor}); ...
Ganancia Sophia: {valor}
Ganancia Mateo: {valor}
```

También es posible imprimir este resultado por la consola, indicándolo por línea de comandos de la siguiente forma:

```bash
python main.py --mostrar-por-consola
```

Lo que también incluirá el tiempo que tomó en ejecutarse el test en milisegundos, pero no cada paso de la solución,
a consideración de que ocuparía mucho espacio en la consola y sería difícilmente legible. Aun así, los pasos sí
quedarán almacenados en el archivo de resultados, más no el tiempo.

**No es necesario** pasar la ruta del archivo de entrada del test por línea de comandos.

Por último, se puede proveer un archivo con los resultados esperados para el test para verificar que la salida es
la esperada, que debe tener extensión `.txt` y tener el mismo formato especificado previamente. Para ello, se debe
indicar por consola de la siguiente forma:

```bash
python main.py --verificar-resultados
```

Lo que imprimirá por consola las diferencias entre el resultado esperado y el resultado obtenido, o indicando
que no hubo diferencias.

Si se quiere tanto mostrar por consola el resultado esperado como verificarlo con un archivo de resultados esperados,
pueden pasarse ambos parámetros por consola en cualquier orden.

Finalmente, si se ejecuta por consola lo siguiente:

```bash
python -m TP2.Tests.test_catedra
```

Se ejecutarán todos los tests proveídos por la catedra, que están en la carpeta `Ejemplos`, se imprimirán sus resultados,
a excepción de los pasos de la solución, el tiempo que tomó el algoritmo para ejecutarse, y se indicará por cada uno
si hubo una diferencia con el resultado esperado, usando de referencia los resultados esperados también proveídos por la
cátedra. Se requiere que **no se modifique ni añada ningún archivo a la carpeta `Ejemplos`**, **ni se remuevan los resultados
esperados de la carpeta `Resultados`**. Luego, se puede añadir cualquier archivo a la carpeta `Resultados` o a la carpeta
`Tests añadidos`.