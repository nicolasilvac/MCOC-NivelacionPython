#forma de codigo con <for>

total = 0
for i in range(1, 5):
	total += i 
print total
#10

#forma de hacer el mismo codigo con un ciclo <while>
total2 = 0
j = 1 			#inicio del while
while j < 5: 	#empieza el j en 1 y llega hasta "antes" de 5
	total2 += j #suma el j actual a la suma anterior
	j += 1 		#avanza el j al siguiente numero
print total2
#10

given_list = [5, 4, 4, 3, 1, -2, -3, -5]

total3 = 0
i = 0
while i < len(given_list) and given_list[i] > 0: 	#recorre los numeros positivos de la lista
	total3 += given_list[i] 						#suma cada elemento al total anterior
	i += 1											#avanza al siguiente elemento
print total3
#17

given_list2 = [5, 4, 4, 3, 1, -2, -3, -5]
total4 = 0
for element in given_list2:
	if element <= 0:			#si el elemento es negativo no lo suma
		break
	total4 += element
print total4
#17

