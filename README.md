# Analise-e-Projeto-de-algoritmos

## Código Primeiro Trabalho:
  ~~~python
 import random
import time
x = 100
vetor = list(range(0,x)) #gera vetor
random.shuffle(vetor)
#print(vetor)
##Cada vX desse corresponde a um algoritmo de ordenação,
# dessa forma é posssivel testar a performace com o mesmo vetor em todos eles!

vs = vetor.copy() #Selection Sort
vq = vetor.copy() #Quick Sort
vc = vetor.copy() #Counting Sort

def selection_sort(vs):
    i = 0
    while i < len(vs) - 1:
        menor = i
        j = i + 1
        while j < len(vs):
            if vs[j] < vs[menor]:
                menor = j

            j += 1

        if menor != i:
            temp = vs[i]
            vs[i] = vs[menor]
            vs[menor] = temp
        i += 1

antes = time.time()
selection_sort(vs)
depois = time.time()
total = (depois - antes)*1000
print("Selection Sort: %10f" % total)

def quick_sort(vq, p, r):
    if p < r: #Condicao de Parada (ou condicao de existencia)
        q = particionar(vq, p, r)
        quick_sort(vq, p, q-1) #Pivotar a Esquerda (Ordenar os elementos menores do que o Pivô)
        quick_sort(vq, q+1, r) #Pivotar a Direita (Ordenar os elementos maiores do que o Pivô)

def particionar(vq, p, r):
    x = vq[p] #Escolhendo o Pivo (É o primeiro elemento da esquerda)
    i = p #Destino final do Pivô
    j =  p + 1 #Contador para percorrer o restante do vetor

    while j<= r: #Percorrer o vetor
        if vq[j] < x: #detectou-se um elemento menor que o pivô, incrementa o i
            i += 1
            trocar(vq, i, j)
        j += 1 #passa para o proximo elemento

    trocar(vq, p, i)

    return i

def trocar(v, n, m):
    temp = vq[n]
    vq[n] = vq[m]
    vq[m] = temp

antes = time.time()
quick_sort(vq, 0, len(vq)-1)
depois = time.time()
total = (depois - antes)*1000
print("Quick Sort %10f" %total)

def countingSort(array):
    tamanho = len(array)
    saida = [0] * tamanho

    # Inicializar o array contador
    contador = [0] * x

    # Guarde a quantidade de cada elemento no array contador
    for i in range(0, tamanho):
        contador[array[i]] += 1

    # Guarda a conta acumulativa
    for i in range(1, 10):
        contador[i] += contador[i - 1]

    # Encontre o index de cada elemento do array original no array contador
    # Coloque os elementos no array de saida
    i = tamanho - 1
    while i >= 0:
        saida[contador[array[i]] - 1] = array[i]
        contador[array[i]] -= 1
        i -= 1

    # Copia os elementos ordenados para o array original
    for i in range(0, tamanho):
        array[i] = saida[i]

antes = time.time()
countingSort(vc)
depois = time.time()
total = (depois - antes)*1000
print("Counting Sort: %10f" % total)
  ~~~
