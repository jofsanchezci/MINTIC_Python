numeros = [1, 3, 6, 9]

while True:
    numero = int(input("Escribe un número del 0 al 9: "))
    if numero >= 0 and numero <= 9:
        break
if numero in numeros:
    print("El número",numero,"se encuentra en la lista",numeros)
else:
    print("El número",numero,"no se encuentra en la lista",numeros)
