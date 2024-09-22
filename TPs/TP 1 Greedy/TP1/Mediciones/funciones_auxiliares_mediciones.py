ruta_absoluta_resultados = 'TP1/Mediciones/resultados.csv'
ruta_absoluta_grafico_medicion_real = 'TP1/Mediciones/grafico_medicion_real.png'
ruta_absoluta_grafico_comparacion = 'TP1/Mediciones/grafico_comparacion.png'
ruta_absoluta_grafico_errores = 'TP1/Mediciones/grafico_errores.png'

def lectura_de_mediciones(linea: str):
    partes = linea.strip().split(',')
    partes[0] = int(partes[0])
    partes[1] = float(partes[1])
    return [partes]