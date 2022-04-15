numeros = [-12, 84, 13, 20, -33, 101, 9]

def separar(lista):
    numeros.sort()
    pares = []
    impares = []
    for n in numeros:
        if n%2 == 0:
            pares.append(n)
        else:
            impares.append(n)
    return pares, impares

pares, impares = separar(numeros)
print(pares
