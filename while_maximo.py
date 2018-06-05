bacterias = int(input("ingrese cantidad minima: "))
dia = 0
vm = int(input("ingrese cantidad maxima : "))

while bacterias < vm:
    aumento = bacterias * 2
    bacterias = aumento
    dia +=1
    print ("Cantidad maxima de bacterias al dia: ",dia)