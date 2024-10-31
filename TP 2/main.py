from TP2.Utilidades.utils_tests import *
from TP2.Utilidades.utils_archivos import *
from TP2.juego_de_las_monedas import resultado_del_juego

if __name__ == '__main__':
    # Los parámetros pasados por línea de comandos
    parametros = verificar_parametros_de_linea_de_comandos()

    # Se usa Tkinter para seleccionar archivos
    ruta = seleccionar_archivo_de_entrada()
    try:
        # Para cargar el archivo con los resultados esperados, lo pedimos antes de ejecutar los test
        if parametros[1]:
            ruta_resultados_esperados = seleccionar_archivo_de_entrada()

        # La carpeta de los resultados es la misma que la de las fuentes
        ruta_resultados_obtenidos = extender_nombre_de_archivo(ruta, RESULTADO, RUTA_RESULTADOS)

        # Guardamos los resultados en un archivo y los devolvemos por si hay que imprimirlos
        resultado = generar_resultados(resultado_del_juego, ruta, ruta_resultados_obtenidos)

        # Si hay que imprimir por consola o comparar con un resultado esperado
        if parametros[0]:
            imprimir_datos_del_test(resultado)
        if parametros[1]:
            comparacion_de_resultados(ruta_resultados_obtenidos, ruta_resultados_esperados)
    except Exception as e:
        print(e)