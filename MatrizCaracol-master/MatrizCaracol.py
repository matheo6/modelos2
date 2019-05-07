# -*- coding: utf-8 -*-

import numpy as np
from io import StringIO


pfile=open('MatrizCaracol','r')
 
data=pfile.read()
 
pfile.close()
 
data=np.genfromtxt(StringIO(data), delimiter  = ',' )

dim= list(data.shape)
fila=dim[0]
columna=dim[1]

derecha=col

inferior=fil

superior=0

izquierda=0


recorridoMatriz=[]
 
print(data)
print(fila)
print(columna) 

while superior < inferior or izquierda < derecha :
    i=inferior-1
    j=derecha-1
    
    while j>izquierda:
        recorrido.append(data[i][j])
        j=j-1
    
    while i>superior:
        recorrido.append(data[i][j])
        i=i-1
        
    while j<derecha-1:
        recorrido.append(data[i][j])
        j=j+1   
    
    while i<inferior-1:
        recorrido.append(data[i][j])
        i=i+1
    
    izquierda=izquierda+1
    
    inferior=inferior-1

    superior=superior+1
    
    derecha=derecha-1


print(recorrido)      
