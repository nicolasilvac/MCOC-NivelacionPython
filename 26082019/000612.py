# uso de diccionarios
d = {} #crea un diccionario
d['George'] = 24	#crea un valor para un determinado string/key			
d['Tom'] = 32		#crea un valor para un determinado string/key
d['Jenny'] = 16		#crea un valor para un determinado string/key

print d['George']
#24
for key, value in d.items():
	print 'key' 
	print key		#imprime el string en este caso, o el item del diccionario
	print 'value'
	print value		#imprime el valor, o lo que esté asociado al item del diccionario
	print ''
#key
#Jenny
#value
#16
#
#key
#George
#value
#24
#
#key
#Tom
#value
#32