import timeit
from random import randint
import matplotlib as mpl


mpl.use('Agg')
import matplotlib.pyplot as plt
def desenhaGrafico(x, y, graphLabel, fileName,xl = "Quantidade de numeros", yl = "Tempo"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x,y, label = graphLabel)
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    fig.savefig(fileName)

def bubbleSort(arr):
	lenght = len(arr)
	for i in range(lenght):
		for j in range(lenght-i-1):
			if arr[j] > arr[j+1]:
				arr[j], arr[j+1] = arr[j+1], arr[j]

def geraListaCrescente(tam):
    lista = []
    i = 0
    while i < tam: 
        lista.append(i)
        i+=1
    return lista

def geraListaDecrescente(tam):
    lista = []
    while tam > 0:
        lista.append(tam)
        tam-=1
    return lista

def geraListaAleatoria(tam):
    lista = []
    while tam > len(lista):
        n = randint(1,1*tam)
        if n not in lista: lista.append(n)
    return lista

x = [1000, 2000, 3000, 4000, 5000]

yMelhorCaso = []
yPiorCaso = []
yMedioCaso = []

for i in x:
  lista = geraListaCrescente(i)
  yMelhorCaso.append(timeit.timeit("bubbleSort({})".format(lista),setup="from __main__ import bubbleSort",number=1))
  
  lista = geraListaDecrescente(i)
  yPiorCaso.append(timeit.timeit("bubbleSort({})".format(lista),setup="from __main__ import bubbleSort",number=1))
  
  lista = geraListaAleatoria(i)
  yMedioCaso.append(timeit.timeit("bubbleSort({})".format(lista),setup="from __main__ import bubbleSort",number=1))

desenhaGrafico(x, yMelhorCaso, 'Melhor caso', 'melhor-caso.png')
desenhaGrafico(x, yPiorCaso, 'Pior caso', 'pior-caso.png')
desenhaGrafico(x, yMedioCaso, 'Medio caso', 'medio-caso.png')
