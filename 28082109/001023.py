import numpy as np 

a = np.array([2,3,4]) #crea un arreglo de una lista de 2, 3 ,4
print a
#[2 3 4]

a = np.arange(1, 12, 2) #crea una lista de rango 1 a 12 con elementos de 2 en 2
print a
#[ 1  3  5  7  9 11]

a = np.linspace(1, 12, 6) #crea una lista de rango de 1 a 12 con 6 elementos equiespaciados
print a
#[  1.    3.2   5.4   7.6   9.8  12. ]

a= a.reshape(3,2) #modifica la lista a una matriz de 3 filas y 2 columnas
print a
#[[  1.    3.2]
# [  5.4   7.6]
# [  9.8  12. ]]

print a.size #imprime el numero de elementos del array
#6

print a.dtype #imprime el tipo de datos del array
#float64

print a.itemsize #imprime cuanto vale cada item del array
#8

b = np.array([(1,5,2,3),(4,5,6)])
print b

print a < 4 #imprime True o False si esque el elemento de a < 4
#[[ True  True]
# [False False]
# [False False]]

print 3*a #multiplica un valor a cada elemento del array
#[[  3.    9.6]
# [ 16.2  22.8]
# [ 29.4  36. ]]

a *= 3 #modifica -a- multiplicandola por 3 cada elemento
print a
#[[  3.    9.6]
# [ 16.2  22.8]
# [ 29.4  36. ]]

a = np.zeros((3,4)) #crea una matriz de 3 filas y 4 columnas de puros 0
print a
#[[ 0.  0.  0.  0.]
# [ 0.  0.  0.  0.]
# [ 0.  0.  0.  0.]]

a = np.ones((10)) #crea una lista de puros 1 de largo 10
print a
#[ 1.  1.  1.  1.  1.  1.  1.  1.  1.  1.]

a = np.zeros((3,4), dtype = np.int16) #mientras menos el int, mas rapido el codigo por ocupar menos memoria

a = np.random.random((2,3)) #crea una matriz de 2 filas y 3 columnas de valores entre 0 y 1
print a
#[[ 0.0806359   0.14877374  0.05633143]
# [ 0.51565635  0.45153668  0.45420591]]

np.set_printoptions(precision = 2, suppress = True) #hace que hayan hasta 2 decimales
print a
#[[ 0.3   0.1   0.15]
# [ 0.9   0.21  0.44]]

a = np.random.randint(0,10,5) #crea una lista de 5 elementos que pueden ir del 0 al 10 inclusive
print a
#[2 9 9 1 9]

print a.min() #a.max #imprime el minimo valor de a
#1

print a.mean() #imprime la media
#4,6

print a.var() #imprime la varianza
#8.0

print a.std() #imprime desviacion estandar
#2.82842712475

a = np.random.randint(1,10,6)
a = a.reshape(3,2)
print a
#[[5 6]
# [2 8]
# [2 7]]

print a.sum(axis=1) #suma las columnas con respecto a 1 eje
#[[5 8]
# [9 9]
# [3 1]]
#[13 18  4]

data = np.loadtxt('data.txt', dtype=np.uint8, delimiter=',', skiprows=1)
print data
#[8 7 7 5 4 3 2] imprime lo escrito en el txt en una lista delimitadas por una coma, saltandose la primera fila (skiprows =1)

a = np.arange(10)
print a
# [0 1 2 3 4 5 6 7 8 9]

print np.random.shuffle(a) #reordena aleatoriamente el arreglo
print a
#[2 9 7 1 8 4 3 6 5 0]

print np.random.choice(a) #elige una opcion al azar del arreglo
#7

print np.random.choice(a)
#8

print np.random.choice(a)
#5

print np.random.random_integers(5, 10, 2) #de una lista de numeros al azar de rango 5 a 10 inclusive, elige 2 aleatoriamente
#[9 7]
print np.random.random_integers(5, 10, 2)
#[6 9]
