suma = 0
numeros = int(input("¿Cuántos números quieres introducir? ") )
for x in range(numeros):
    suma += float(input("Introduce un número: ") )
print("Se han introducido",numeros,"números que en total han sumado",suma,"y la media es",suma/numeros)
