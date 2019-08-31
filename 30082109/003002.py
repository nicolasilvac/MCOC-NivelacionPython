from matplotlib import pyplot as plt
plt.style.use('ggplot') #cambia el formato del grafico

dev_x = [25,26,27,28,29,30,31]

dev_y = [20020,23030,40400,50505,60606,70700,80800]

dev_hdhd = [30020,43030,50400,60505,70606,80700,90800]
print len(dev_x), len(dev_y) #deben tener el mismo tamano

plt.plot(dev_x,dev_y) #plt.plot(eje x, eje y)
plt.plot(dev_x,dev_hdhd) #puede imprimir dos o mas curvas en un grafico
plt.show() #imprime el grafico

plt.xlabel('Ages') #nombre eje x
plt.ylabel('Salario') #nombre eje y
plt.title('Salario promedio') #titulo grafico


plt.plot(dev_x,dev_y, color= 'k', linestyle = '--', label = 'Python') #plt.plot(eje x, eje y, color, estilo de linea, nombre de curva)
plt.plot(dev_x,dev_hdhd) #puede imprimir dos o mas curvas en un grafico
plt.show() #imprime el grafico

plt.xlabel('Ages') #nombre eje x
plt.ylabel('Salario') #nombre eje y
plt.title('Salario promedio') #titulo grafico

plt.style.use('fivethirtyeight') #cambia el formato del grafico

dev_x = [25,26,27,28,29,30,31]

dev_y = [20020,23030,40400,50505,60606,70700,80800]

dev_hdhd = [30020,43030,50400,60505,70606,80700,90800]
print len(dev_x), len(dev_y) #deben tener el mismo tamano

plt.plot(dev_x,dev_y) #plt.plot(eje x, eje y)
plt.plot(dev_x,dev_hdhd) #puede imprimir dos o mas curvas en un grafico
plt.show() #imprime el grafico

plt.xlabel('Ages') #nombre eje x
plt.ylabel('Salario') #nombre eje y
plt.title('Salario promedio') #titulo grafico


plt.plot(dev_x,dev_y, color= 'k', linestyle = '--', label = 'Python') #plt.plot(eje x, eje y, color, estilo de linea, nombre de curva)
plt.plot(dev_x,dev_hdhd) #puede imprimir dos o mas curvas en un grafico
plt.show() #imprime el grafico

plt.xlabel('Ages') #nombre eje x
plt.ylabel('Salario') #nombre eje y
plt.title('Salario promedio') #titulo grafico

plt.legend()
plt.tight_layout() 
plt.savefig('plot.png') #guarda el grafico como imagen .png