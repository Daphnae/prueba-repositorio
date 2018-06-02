n = int(input("Ingrese la cantidad de cauchos a comprar: "))
p = float(input("Ingrese el precio unitario: "))
if n > 6:
    p = 0.15 * p
else:
    p = 0.1 * p
total =n * p
print("El total a pagar es: " ,total)
