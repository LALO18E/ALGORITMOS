def busqueda_lineal(A, valor):

    comparaciones = 0
    for i in range(len(A)):
        comparaciones += 1
        if A[i] == valor:
            return i, comparaciones
    return -1, comparaciones

# ==================================================

A = [4, 7, 1, 9, 3, 6]

# Prueba 1 sí está en:
valor = 9
Posicion, compara = busqueda_lineal(A, valor)
print(f"Buscando {valor} en {A}")
print(f"Posición encontrada: {Posicion}")
print(f"Número de comparaciones: {compara}\n")

# Prueba 2 valor que no está:
valor = 5
Posicion, compara = busqueda_lineal(A, valor)
print(f"Buscando {valor} en {A}")
print(f"Posición encontrada: {Posicion}")
print(f"Número de comparaciones: {compara}\n")

# Prueba 3 valor en la primera posición (mejor caso):
valor = 4
Posicion, compara = busqueda_lineal(A, valor)
print(f"Buscando {valor} en {A}")
print(f"Posición encontrada: {Posicion}")
print(f"Número de comparaciones: {compara}\n")