# -*- coding: utf-8 -*-

#funcion para el calculo del momento de inercia de una seccion cuadrada

def Inercia(b,h):
    Inercia = b*h**3/12 #Se hace la ecuacion
    return Inercia #Retorna el valor de la ecuacion de la Linea 7

b = 20 #cm
h = 30 #cm

print 'Inercia de la seccion cuadrada = ', Inercia(b,h), "cm4"

#RESULTADOS
#Inercia de la seccion cuadrada =  45000 cm4