#Ejemplo de listas

a = [1, 2, 3, 4, 5, 6]
b = ['a', 'b', 'c', 'd', 'e', 'f']
c = [['ab',00],['cd',11]]

#Para imprimir el primer elemento de cada lista
print a[0], ',' , b[0], ',' ,  c[0]
#Resultado: 1 , a , ['ab', 0]

#Para re-escribir el segundo termino de cada lista
a[1], b[1], c[1] = b[1] , c[1], a[1]
print a[1], ',' , b[1], ',' ,  c[1]
#Resultado: b , ['cd', 11] , 2

#Conclusion: las listas pueden tener floats, string, o listas (hasta ahora), y sus terminos se pueden redefinir utilizando a[n]=numero