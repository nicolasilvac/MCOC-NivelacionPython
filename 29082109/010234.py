import numpy as np 

a = np.array([1.,2.,3.,4.])
b = np.array([10.,11.,12.,13.])

print a + b #suma de listas/vectores
#[11 13 15 17]

print a / b #division de listas/vectores
#[ 0.1         0.18181818  0.25        0.30769231]

print a ** b #eleva elemento con elemento de otra lista correspondiente
#[  1.00000000e+00   2.04800000e+03   5.31441000e+05   6.71088640e+07]

print a.ndim #imprime las dimensiones
#1

print a.shape #imprime los elementos por dimension
#(4,)

f = 5
print type(f)
#int
f = (1,2)
print type(f)
#tuple
print a * 100
#[ 100.  200.  300.  400.]
c = np.array([[10,11,12],[20,21,22]]) #crea una matriz
print c
#[[10 11 12]
# [20 21 22]]

print c.shape
#(2,3) contiene 2 filas y 4 columnas

print c[0,0] #imprime el valor en la fila 0 columna 0
#10

print c[0] #imprime la fila 0
#[10 11 12]
a = np.array([10,11,12,13,14])
print a[1:3] #imprime desde el elemento 1 al 3
#[11 12]
print a[:3] #imprime desde el inicio hasta el elemento 3
#[10 11 12]
print a[-2:] #imprime desde el penultimo elemento hasta el ultimo elemento
#[13 14]
print a[::2] #imprime todos los elementos de 2 en 2
#[10 12 14]

a = np.arange(25).reshape(5,5) #crea una matriz del 0 al 25 de 5x5
print a
#[[ 0  1  2  3  4]
# [ 5  6  7  8  9]
# [10 11 12 13 14]
# [15 16 17 18 19]
# [20 21 22 23 24]]

red= a[:, 1::2] #(todas las filas, desde la columna 1 de dos en dos)
print red
#[[ 1  3]
# [ 6  8]
# [11 13]
# [16 18]
# [21 23]]
yellow = a[4]
yellow = a[-1]
yellow = a[-1, :] #imprime lo mismo pero este transmite al usuario que es 2D
print yellow
#[20 21 22 23 24] #la ultima fila

blue = a[1::2, :-1:2] #las filas desde la 1 de 2 en 2 y las columnas desde la 2 a la ultima pero desde la ultima
print blue
#[[ 5  7]
# [15 17]]

a = np.array([3,-1,-2,4,-5,8])
print a

negativos = a<0
print negativos #imprime true o false si es menor a 0
#[False  True  True False  True False]

print a[a<0] #imprime los elementos menor a 0
#[-1 -2 -5]

a[a<0]=0 #los menores a 0 los convierte en 0
print a
#[3 0 0 4 0 8]

print (a<8).any() #imprime si algun elemento es menor a 8
#True
print (a>3) & (a<8) #imprime los requeridos
#[False False False  True False False]

print a
#[3 0 0 4 0 8]

print np.nonzero(negativos) #imprime los que no son 0
a.sort() #ordena de menor a mayor
print a
#[0 0 0 3 4 8]

a = np.array([10, 1, 20])
subset = a[[0, 2]] #asigna el elemento 0 y 2 al arreglo subset
print subset
#[10 20]
subset[0]=-1
print subset
#[-1 20]
a = np.arange(36).reshape(6,6)
print a 
output=np.empty_like(a, dtype='float')
output.fill(np.nan)
print np.where(a%3==0, a, np.nan) #imprime todos los multiplos de 3 sino los deja como nan
#[[  0.  nan  nan   3.  nan  nan]
# [  6.  nan  nan   9.  nan  nan]
# [ 12.  nan  nan  15.  nan  nan]
# [ 18.  nan  nan  21.  nan  nan]
# [ 24.  nan  nan  27.  nan  nan]
# [ 30.  nan  nan  33.  nan  nan]]

a = np.arange(24).reshape(6, 4)
print a.shape
#(6, 4)
print a.mean(axis=0).shape #imprime el promedio para el eje 0
#(4,)

