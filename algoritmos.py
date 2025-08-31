def par_suma_ordenando(A, K):
    B = sorted(A)  
    i, j = 0, len(B) - 1

    while i < j:
        suma = B[i] + B[j]
        if suma == K:
            return True, (B[i], B[j])
        elif suma < K:
            i += 1
        else:
            j -= 1
    return False, None

A = [3, 5, 4, 2, 8, 1, 6, 7, 10, 11]
K = 18

existe, par = par_suma_ordenando(A, K)
if existe:
    print(f"✅ Existe un par que suma {K}: {par[0]} + {par[1]} = {K}")
else:
    print(f"❌ No existe ningún par que sume {K}")
