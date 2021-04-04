print("calculo del siguente número primo")

numero=int(input("introduzca un número primo"))
numeroinicial=numero
boolean=True
siguiente=1

while boolean==True:
   
    numero=numero+1;
    
    for i in range (2,numeroinicial):
        
        módulo=numero%i
        #print("módulo")
        print(módulo)
        if módulo==0:
            break
        
        if módulo!=0 and i==numeroinicial-1:
            boolean=False
            siguiente=numero
            break
        
    #print("numero")
    print(numero)
print("numero primo siguiente")    
print(siguiente) 
   