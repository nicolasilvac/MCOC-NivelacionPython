#Ejemplo youtube

a = [3, 10, -1]
print a
#[3, 10, -1]

a.append(1) #agrega un elemento al ultimo lugar de la lista
print a
#[3, 10, -1, 1]

a.append('hello')
print a
#[3, 10, -1, 1, 'hello']

a.append('[1,2]')
print a
#[3, 10, -1, 1, 'hello', '[1,2]']

a.pop() #borra el ultimo elemento de la lista
print a
#[3, 10, -1, 1, 'hello']

a.pop()
print a
#[3, 10, -1, 1]

print a[0] #imprime el primer elemento de la izquierda de la lista
print a[3] #imprime el cuarto elemento de la izquierda de la lista

a[0]=100 #re-define el elemento en el lugar 0 por el valor 100

print a
#[100, 10, -1, 1]

b = ['banana', 'apple', 'microsoft'] #lista de strings

temp = b[0]
print temp 
#banana

