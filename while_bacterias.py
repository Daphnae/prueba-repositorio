bacterias = 5 #Cambia la cantiada minima
dia = 0
vm = 80

while bacterias <= vm:
    aumento = bacterias * 2
    bacterias = aumento
    dia +=1
    print ("Cantidad maxima de bacterias al dia: ",dia)