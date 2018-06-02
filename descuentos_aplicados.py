n = int(input("Ingrese la cantidad de confort: "))
p = int(input("Ingrese el precio unitario: "))
if (n==5) or (n<=9):
    valor = n * p
    desc = valor * 0.20
    total = valor-desc
elif (n==1) or (n<=4):
    valor = n * p
    desc = valor* 0.15
    total = valor-desc
else: 
    valor = n * p
    desc = valor * 0.25
    total = valor-desc
print("El valor total a pagar: ",total)
