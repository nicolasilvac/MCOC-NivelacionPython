#tarea propuesta en el video
#can you compute all multiples of 3, 5 that are less than 100?
lista= list(range(1, 100))

#respuesta

suma = 0
for elemento in lista:
	if elemento % 3 == 0 or elemento % 5 == 0:
		suma += elemento
print suma
#Resultado 2318