# Importamos la libreria random
import random

# Pedimos al usuario que digite la cantidad de numeros que tendra el txt
print("Cantidad de numeros en el arreglo:")
num = input()
num = int(num)
num1 = num

# Inicializamos el archivo de texto, el arreglo de numeros con parametros 
# de crear numeros hasta el valor de num y este primer valor lo anexamos 
# al archivo txt
outfile = open('numeros.txt', 'w')
numeros = [0]
outfile.writelines(str(numeros[0])+" ")

# Inicializamos la variable del ciclo while
i=1

# Creamos el arreglo de numeros de tamaño num y lo vamos incrementando
# hasta tener todo el arreglo lleno
while i<num:
    valor=numeros[i-1]+1
    numeros.append(valor)
    i+=1

# Acomodamos aletoriamente cada valor en el arreglo
random.shuffle(numeros)

# Regresamos a 1 el valor de i
i=1

# Escribimos el arreglo en el txt separado con espacio
while i<num1:
    outfile.writelines(str(numeros[i])+" ")
    i+=1







