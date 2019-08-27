import numpy as np
from skimage import io

photo = io.imread('hola.png')
print type(photo)
#<numpy.ndarray> #convierte una imagen en una matriz

print photo.shape
#(324, 574, 3)

import matplotlib.pyplot as plt
plt.imshow(photo)
#imprime la imagen 'hola.png'

plt.imshow(photo[::-1])
#imprime la imagen dada vuelta

plt.imshow(photo[:,::-1])
#imprime la original

photo_sin = np.sin(photo)
#a cada valor de la matriz le aplica la funcion sin()

print(np.sum(photo))#print suma todos los elementos
print(np.prod(photo))#multiplica todos los elementos

#al poner funciones como np.funcion(photo) estas se aplican a todos los valores de la matriz

a_array = 10
b_array = 20

print a_array@b_array #multiplica los arreglos

np.sort(a) #arregla los datos de menor a mayor