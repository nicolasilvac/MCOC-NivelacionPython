import numpy as np 

a = np.zeros(3) #crea una matriz de 1 fila y 3 columnas
print a
#[ 0.  0.  0.]
print type(a[0]) #entrega el tipo de elemento numero 0 del array a
#<type 'numpy.float64'>

z = np.zeros(10)
print z
#[ 0.  0.  0.  0.  0.  0.  0.  0.  0.  0.]

z.shape = (10, 1) #cambia la forma del array
print z
#[[ 0.]
# [ 0.]
# [ 0.]
# [ 0.]
# [ 0.]
# [ 0.]
# [ 0.]
# [ 0.]
# [ 0.]
# [ 0.]]
x = np.linspace(2, 10, 5) #crea un arreglo del 2 al 10 dividido en 5 elementos
print x	#sirve para usarlos como ejes 
#[  2.   4.   6.   8.  10.]

y = np.array([10, 20]) #crea una matriz con una fila con 10 20
print y
#[10 20]

b_list = [1,2,3,4,5,6,7]
b = np.array([b_list]) #crea la lista b_list como un arreglo
print b
#[[1 2 3 4 5 6 7]] matriz, no lista

c_list = [[1,2,3,4,5,6,7],[11,22,33,44,55,66,77]]
c = np.array([c_list])
print c
#[[[ 1  2  3  4  5  6  7]
# [11 22 33 44 55 66 77]]] crea una matriz de 2 filas y 7 columnas

np.random.seed(0)
x1 = np.random.randint(10, size = 6) #crea un arreglo de 6 elementos con numeros aleatorios de 0 a 10
print x1
#[5 0 3 3 7 9]

print x1[1]
# 0
print x1[0:2] #retorna desde el elemento 0 al elemento 2-1
#[5 0]
print x1[0:3] #retorna desde el elemento 0 al elemento 3-1
#[5 0 3]
print x1[-1]
#9 retorna el ultimo elemento

