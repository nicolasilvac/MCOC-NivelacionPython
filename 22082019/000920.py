a = ['banana', 'apple', 'microsoft']

for elemento in a:
	print elemento #imprime cada elemento de la lista
#banana
#apple
#microsoft

b = [20, 10, 5]
total = 0
for e in b:
	total = total + e #cada "e" toma el elemento numero e de la lista (en este caso son floats por lo que se pueden sumar)
print total
#35 (la suma total)

c = list(range(1,5)) #crea una lista desde el 1 al 4, no cuenta el 5
print c
#[1, 2, 3, 4]

total2 = 0
for i in range(1, 5):
	total2 += i #me ahorro tener que poner total2 = total2 + i
print total2
#10

print(list(range(1, 8)))
#[1, 2, 3, 4, 5, 6, 7]

total3 = 0
for i in range(1, 8):
	if i % 3 == 0: 
		total3 += i #suma los restos
print total3
#9

