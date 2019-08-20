# -*- coding: utf-8 -*-
import math
#Determinacion de figuras geometricas y su area es apropiada para ser pintada

Area_Pint = 40 #m2, area que puede pintar un tarro de pintura

a = 6 #ancho
b = 7 #base
r = 3 #radio

Area_Cuadrado = a**2
Area_Rectangulo = a*b
Area_Circulo = r**2*math.pi

#Si el area que puede pintar un tarro de pintura es mayor al area de la figura, esta SI puede ser pintada
if Area_Cuadrado < Area_Pint:
    print 'El Cuadrado SI puede ser pintado'
elif Area_Cuadrado > Area_Pint:
    print 'El Cuadrado NO puede ser pintado'
if Area_Rectangulo < Area_Pint:
    print 'El Rectangulo SI puede ser pintado'
elif Area_Rectangulo > Area_Pint:
    print 'El Rectangulo NO puede ser pintado'
if Area_Circulo < Area_Pint:
    print 'El Circulo SI puede ser pintado'
elif Area_Circulo > Area_Pint:
    print 'El Circulo NO puede ser pintado'

