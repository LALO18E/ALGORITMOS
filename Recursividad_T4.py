# 1. suma recursiva de una lista de enteros
def suma_lista(lista):
   
    if not lista: 
        return 0
    return lista[0] + suma_lista(lista[1:])

# 2. contar los dígitos de un entero positivo
def contar_digitos(n):
    
    if n < 10:
        return 1
    return 1 + contar_digitos(n // 10)

# 3. eliminar de una pila el valor en la posición media
def eliminar_medio(pila, k=None):
    if not pila:
        return None
    if k is None:
        k = len(pila) // 2
    if k == 0:
        return pila.pop()
    tope = pila.pop()
    eliminado = eliminar_medio(pila, k-1)

    pila.append(tope)
    return eliminado

# 4. verificar si una cadena es palíndromo con recursividad
def es_palindromo(cadena):
    if len(cadena) <= 1:
        return True
    if cadena[0] != cadena[-1]:
        return False
    return es_palindromo(cadena[1:-1])

# ------------------------------------------ EJEMPLOS DE LOS 4 EJERCICIOS ------------------------------------------

if __name__ == "__main__":
    # 1) Suma recursiva
    nums = [1, 2, 3, 4, 5]
    print("Suma recursiva:", suma_lista(nums))
    print()

    # 2) Contar dígitos
    n = 12345
    print("Número de dígitos en", n, ":", contar_digitos(n))
    print() 

    # 3) Eliminar elemento medio de pila
    pila = [1, 2, 3, 4, 5]
    print("Pila original:", pila)
    eliminado = eliminar_medio(pila)
    print("Eliminado:", eliminado)
    print("Pila final:", pila)
    print()

    # 4) Palíndromo
    print("¿La frase 'radar' es palíndromo?:", es_palindromo("radar"))
    print("¿La frase 'python' es palíndromo?:", es_palindromo("python")) 
