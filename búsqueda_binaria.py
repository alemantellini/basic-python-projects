import random
import time

def búsqueda_ingenua(lista, objetivo):
    """Búsqueda ingenua de un valor en una lista."""
    for i in range(len(lista)):
        # range(len(lista)) --> 0, 1, 2, 3, ..., len(lista)-1
        if lista[i] == objetivo:
            return i
    return -1

mi_lista = [1, 3, 5, 10, 12]
print(búsqueda_ingenua(mi_lista, 10))