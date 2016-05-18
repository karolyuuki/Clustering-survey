import math
import random

def distanciaeuclidiana(i,j):
    #Calculates the distance between two points
    n = len(i)
    soma = 0
    for a in range(n):
        soma = soma + ((j[a] - i[a])**2)
    distancia = math.sqrt(soma)
    return distancia

def dissimilarity(i):
    prox = distanciaeuclidiana(i,i)
    if (prox == 0):
        return 1
    else:
        return 0

def simmetry(i,j):
    
    prox = distanciaeuclidiana(i,j)
    if (prox == 0):
        return 1
    else:
        return 0

def positivity(i,j):
    
    prox = distanciaeuclidiana(i,j)
    if (prox >= 0):
        return 1
    else:
        return 0

def triinequa(i,j,k):
    prox1 = distanciaeuclidiana(i,j)
    prox2 = distanciaeuclidiana(i,k)
    prox3 = distanciaeuclidiana(k,j)
    print(prox1)
    print(prox2)
    print(prox3)
    if (prox1 <=(prox2+prox3)):
        return 1
    else:
        return 0
    
def equality(i,j):
    prox = distanciaeuclidiana(i,j)
    if (prox==0):
        for x,y in zip(i,j):
            if (x!=y):
                return 0
            else:
                return 1
    else:
        return 2
                
                
