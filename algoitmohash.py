def encontrar_par_con_suma_k(array, K):
    diccionario = {}

    for elemento in array:
        complemento = K - elemento
        if complemento in diccionario:
            return True, (complemento, elemento) 
        diccionario[elemento] = True

    return False, None  
array = [3, 5, 4, 2, 8, 1, 6, 7, 10, 11]
K = 18

existe, par = encontrar_par_con_suma_k(array, K)

if existe:
    print(f"✅ Existe un par que suma {K}: {par[0]} + {par[1]} = {K}")
else:
    print(f"❌ No existe ningún par que sume {K}")
