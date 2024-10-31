import numpy as np

def complejidad(n):
    return n**2

def determinar_coeficientes(funcion, mediciones) -> list:
    A = np.array([[funcion(medicion[0]), 1] for medicion in mediciones])
    b = np.array([medicion[1] for medicion in mediciones])

    AtA = A.T @ A # A transpuesta * A
    Atb = A.T @ b # A transpuesta * b

    return np.linalg.inv(AtA) @ Atb # Coeficientes == Inversa(A transpuesta por A) * (A transpuesta por b)

def errores(aproximacion, mediciones) -> list:
    errores = [np.abs(aproximacion(medicion[0]) - medicion[1]) for medicion in mediciones]
    error_cuadratico_total = np.sum([error ** 2 for error in errores])
    return errores, error_cuadratico_total

def funcion_aproximadora(funcion_original, mediciones):
    coeficientes = determinar_coeficientes(funcion_original, mediciones)

    def funcion_final(n):
        return coeficientes[0] * funcion_original(n) + coeficientes[1]

    return funcion_final