# -*- coding: utf-8 -*-
"""Trabalho de implementação II.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tVA3KdstVZTFaK6TwAc_zizQUNBWKRaN

## dijkstra:
"""

# declaração das bibliotecas 
from collections import defaultdict
from heapq import *
import time
import random

# Setando o tempo inicial para calcularmos o tempo total posteriormente
antes = time.time_ns() / (10 ** 9)

# Declarando a função do dijkstra
def dijkstra(edges, f, t):
   
   # preparação das variáveis pro algoritmo
    g = defaultdict(list)
    for l, r, c in edges:
        g[l].append((c, r))

    q, seen, mins = [(0, f, ())], set(), {f: 0}

    # loop para percorrer a lista
    while q:
        (cost, v1, path) = heappop(q)
        # verifica se o nodo já foi visto ou não e se ele não ele é colocado na lista de visto
        if v1 not in seen:
            seen.add(v1)
            path = (v1, path)
            # se o nodo atual for o nodo final buscado ele retorna o custo e caminho até ele.
            if v1 == t:
                return (cost, path)

            # loop para percorrer o grafo e modifcar valores que ja foram vistos se tem um caminho mais curto até eles
            for c, v2 in g.get(v1, ()):
                if v2 in seen:
                    continue

                # Pega o valor do nodo anterior  
                prev = mins.get(v2, None)
                next = cost + c

                # verifica se o nodo anterior tem valor menor e coloca no nodo
                if prev is None or next < prev:
                    mins[v2] = next
                    heappush(q, (next, v2, path)) # joga o nodo pro final da fila

    return float("inf")


if __name__ == "__main__":

# Fazendo a declaração do grafo utilizado, chamar a função e printar sua distância 
    n = 10
    grafo1 = [
        ('Argentina', 'Brasil', random.randrange(0, n)),
        ('Brasil', 'Uruguay', random.randrange(0, n)),
        ('Uruguay', 'Argentina', random.randrange(0, n)),
        ('Chile', 'Bolivia', random.randrange(0, n)),
        ('Bolivia', 'Venezuela', random.randrange(0, n)),
        ('Venezuela', 'Brasil', random.randrange(0, n)),
        ('Equador', 'Peru', random.randrange(0, n)),
        ('Paraguai', 'Argentina', random.randrange(0, n)),
        ('Peru', 'Brasil', random.randrange(0, n)),
        ('Brasil', 'Venezuela', random.randrange(0, n)),
        ('Argentina', 'Chile', random.randrange(0, n)),
        ('Chile', 'Peru', random.randrange(0, n)),
        ('Bolivia', 'Brasil', random.randrange(0, n)),
        ('Peru', 'Equador', random.randrange(0, n)),
        ('Peru', 'Colombia', random.randrange(0, n))
    ]


    print("Argentina -'> Venezuela',:")
    print("A menor distancia para o grafo um e: ",
          dijkstra(grafo1, "Argentina", "Venezuela"))

# Calcula o tempo de execução e printa na saída
    depois = time.time_ns() / (10 ** 9)
    total = (depois - antes)
    print(total)

"""## Bellman-Ford:"""

# importando bibliotecas necessárias
import time
import random

# declaração da função bellman-ford
def bellman_ford(graph, source):

    # Setando o caso base
    distance, predecessor = dict(), dict()
    for node in graph:
        distance[node], predecessor[node] = float('inf'), None
    distance[source] = 0

    # Uma loop para percorrer todo o grafo
    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbour in graph[node]:

                # Verifica a distância entre o nodo e todos os nodos visinhos e coloca na variável distancia, juntamente com o nodo que a distância foi calculada
                if distance[neighbour] > distance[node] + graph[node][neighbour]:
                    distance[neighbour], predecessor[neighbour] = distance[node] + \
                        graph[node][neighbour], node

    # um loop para percorrer o grafo quando temos pesos negativos
    for node in graph:
        for neighbour in graph[node]:
            assert distance[neighbour] <= distance[node] + \
                graph[node][neighbour], "Negative weight cycle."

    #retorna os resultados encontrados que são a distancia e o nodo 
    return distance, predecessor


if __name__ == '__main__':

# declarando a variável para calcular o tempo de execução do código
    antes = time.time_ns() / (10 ** 9)

# Fazendo a declaração do grafo utilizado, chamar a função e printar sua distância 
    n = 10
    grafo = {
        'Argentina': {'Chile': random.randrange(0, n), 'Bolivia': random.randrange(0, n), 'Uruguay': random.randrange(0, n), 'Brasil': random.randrange(0, n), 'Paraguay': random.randrange(0, n) },
        'Brasil': {'Venezuela': random.randrange(0, n), 'Bolivia': random.randrange(0, n)},
        'Uruguay': {'Brasil': random.randrange(0, n)},
        'Bolivia': {'Brasil': random.randrange(0, n), 'Peru': random.randrange(0, n)},
        'Chile': {'Bolivia': random.randrange(0, n),'Peru': random.randrange(0, n)},
        'Peru': {'Equador': random.randrange(0, n)},
        'Venezuela': {'Colombia': random.randrange(0, n)},
        'Equador': {'Peru': random.randrange(0, n)},
        'Colombia': {'Equador': random.randrange(0, n)},
        'Paraguay': {'Brasil': random.randrange(0, n)},
    }

    distance1, predecessor = bellman_ford(grafo, source='Argentina')
    print(distance1, '\n')

# Calcula o tempo de execução e printa na saída
    depois = time.time_ns() / (10 ** 9)
    total = (depois - antes)
    print(total)

"""## Mochila Binária ou Booleana"""

# importando as bibliotecas necessárias
import time

# declarando a função da mochila booleana
def knapSack(W, wt, val, n):

    # verificando se a capacidade e o número de itens são nulos
    if n == 0 or W == 0:
        return 0

    # se o peso passar da capacidade da mochila ele uma chamada recursiva da função
    if (wt[n-1] > W):
        return knapSack(W, wt, val, n-1)

    # senão passar a capacidade ele retorna o valor que máximiza o lucro.
    else:
        return max(
            val[n-1] + knapSack(
                W-wt[n-1], wt, val, n-1),
            knapSack(W, wt, val, n-1))

# inicializando as variáveis
val = []
wt = []
n = 500

# fazendo a criação dos itens e colocando valores aleatórios para as variáveis valor e peso do item
for i in range(n):
    val = [x*3 for x in range(0, n)]
    wt = [x*2 for x in range(0, n)]

# printa o valor máximo obtido usando as variáveis dadas
antes = time.time_ns() / (10 ** 9)
print("Valor maximo:", knapSack(100, wt, val, n))

# printa o tempo final de execução do algoritmo
depois = time.time_ns() / (10 ** 9)
total = (depois - antes)
print(total)

"""## Mochila Fracionária:"""

# importando as bibliotecas necessárias
import time

# declarando a função da mochila fracionária
def fractional_knapsack(value, weight, capacity):

    # organizando os dados
    index = list(range(len(value)))
    ratio = [v/w for v, w in zip(value, weight)]
    index.sort(key=lambda i: ratio[i], reverse=True)

# inicialização dos valores de saída
    max_value = 0
    fractions = [0]*len(value)

    # loop para percorrer o grafo
    for i in index:
        # verificar se é necessário particionar o item ou não
        if weight[i] <= capacity:
            fractions[i] = 1
            max_value += value[i]
            capacity -= weight[i]
        # se for necessário ele faz partição para dar o maior valor possivel
        else:
            fractions[i] = capacity/weight[i]
            max_value += value[i]*capacity/weight[i]
            break

# retorno dos valor máximo obtido e as partições
    return max_value, fractions

# inicia as variáveis
n = 600
weight1 = []
value1 = []
capacity = 300

# fazendo a criação dos itens e colocando valores aleatórios para as variáveis valor e peso do item
for i in range(n):
    value1 = [x*3 for x in range(1, n)]
    weight1 = [x*2 for x in range(1, n)]


# printa o valor máximo obtido usando as variáveis dadas
antes = time.time_ns() / (10 ** 9)
max_value, fractions = fractional_knapsack(value1, weight1, capacity)
print('Maximo de valor que pode ser carregado:', max_value)

# printa o tempo final de execução do algoritmo
depois = time.time_ns() / (10 ** 9)
total = (depois - antes)
print(total)