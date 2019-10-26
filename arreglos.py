class Arreglos:
    lista1 =[]
    lista2 =[]
    cantidad = int(input("cantidad arreglo 1: "))
    cantidad2 = int(input("cantidad arreglo 2: "))
    mayor1 =0
    mayor2 =0
    mayorFinal =0
    i =1
    while(cantidad>0):
        numero = float(input("numero #" + str(i) + ": "))
     
        lista1.append(numero)
        i = i +1 
        cantidad = cantidad -1
    mayor1 = max(lista1)
  
    
    j =1
    while(cantidad2>0):
        numero = float(input("numero #" + str(j) + ": "))
  
        lista2.append(numero)
        j = j +1 
        cantidad2 = cantidad2 -1
    mayor2 = max(lista2)
    
    
    if mayor1 > mayor2:
         mayorFinal = mayor1
    else:
         mayorFinal = mayor2
        # TODO: write code...
    print("estos son los numeros ingresados lista 1: ", lista1)
    print("Dato mayor lista 1 :", mayor1)
    print ("-------------------------------------------")
    print("estos son los numeros ingresados lista 2: ", lista2)
    print("Dato mayor lista 2:", mayor2)
    print ("El dato mayor es: " , mayorFinal)
    
    
    
 """arreglo = [1, 2, 3, 4, 5]
nuevo_arreglo = [i * 2 for i in arreglo]

print (nuevo_arreglo) """
    