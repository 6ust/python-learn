#Algoritmo para aleatorização de posiçoes de um vetor.
from random import randint

result = []

limit = int(input("Por Favor, informe um limite para o vetor"))

while len(result) != limit + 1:
    r = randint(0, limit)
    if r not in result:
        result.append(r)

print(result)