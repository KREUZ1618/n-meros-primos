#funciones
def suma (matriz1,matriz2):
    
    rows = len(matriz2)
    columns = len(matriz2[0])
    
    matriz3 = []
    
    for i in range (rows):
      matriz3.append( [0] * columns)
    
    
    for i in range(rows):
            for  j in range(columns):
                    matriz3[i][j] += matriz1[i][j] + matriz2[i][j]
                    
                    
    print ('la matriz resultante es')
    print (matriz3)


def producto (matriz1,matriz2):
    
    rows = len(matriz2[0])
    columns = len(matriz1)
    
    matriz3 = []
    
    for i in range (rows):
      matriz3.append( [0] * columns)
    
    for x in range(columns):
        for i in range(columns):
            for  j in range(rows):
                    matriz3[i][x] += matriz1[i][j]*matriz2[j][x]
                    
                    
    print ('el resultado es')
    print (matriz3)
    
    
def matriz ():
    
   filas = int(input ("Introduzca el numero de filas"))
   columnas = int(input ("Introduzca el numero de columnas"))
   
   matriz1 = []
 
    
   for i in range (filas):
      matriz1.append( [0] * columnas) 
    
   print ('Ingrese su Matriz 1')
   for i in range(filas):
          for j in range(columnas):
              matriz1[i][j] = float(input('Elemento (%d,%d): ' % (i, j)))
                    
                        
   print ('la matriz es')
   print (matriz1)
   return matriz1

#para matrices de nxn
def determinante (matriz):
   
   matrizaux=[]
   
   g=0
   h=0
 
   deter=0
   
   tamaño=len(matriz)
   tamaño2=tamaño-1
    
   for i in range (tamaño2):
       matrizaux.append( [0] * tamaño2) 
       
   
    
   if len(matriz)>2:
       
       
     #se itera sobre la fila 0  
    for i in range ((tamaño)):
       
       
       
       for j in range (tamaño):
           
            
           
           for k in range (tamaño):
               
               print("i"+str(i))
               print("j"+str(j))
               print("k"+str(k))
              
           
           #se construye la matriz menor 
           
               if j!=0 and k!=i:
                  
                  if g==tamaño2:       
                                 g=0
                                 h+=1
                                 
                  print("g"+str(g))
                  print("h"+str(h)) 
                  if h==tamaño2:       
                                 h=0
                                 
                  matrizaux[h][g]=matriz[j][k]
                  g+=1
                             
                   
      #aquí se utiliza la recurrencia para calcular el determinante de la matriz menor
       deter+=pow(-1,i+2)*matriz[0][i]*determinante(matrizaux)
       print(deter)
       print(matrizaux)
   
   if tamaño==2:
                 
       deter+=matriz[0][0]*matriz[1][1]-matriz[1][0]*matriz[0][1]             
   
   return deter




#main

print("determinante")

print("introduzca una matriz de nxn")

matriz1=matriz()

print(determinante(matriz1))

print("producto")

matriz1=matriz()

matriz2=matriz()

producto(matriz1,matriz2)

print("suma")

matriz1=matriz()

matriz2=matriz()

suma(matriz1,matriz2)

