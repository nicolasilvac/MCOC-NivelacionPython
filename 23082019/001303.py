#tarea propuesta por el video

#sumar todos los terminos positivos y negativos por separado de la lista dada
given_list3 = [7, 5, 4, 4, 3, 1, -2, -3, -5, -7]

sumaPositivos = 0
sumaNegativos = 0
i = 0
while i < len(given_list3):
	if given_list3[i] > 0:					#si el elemento es positivo
		sumaPositivos += given_list3[i]
		i += 1
	elif given_list3[i] < 0:				#si el elemento es negativo
		sumaNegativos += given_list3[i]
		i += 1		
print sumaPositivos, sumaNegativos
#Resultado: sumaPositivos = 24, sumaNegativos = -17



