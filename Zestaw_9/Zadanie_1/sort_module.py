import random


def insert_sort(lista):
    for i in range(1, len(lista)):
        for j in range(i, 0, -1):
            if lista[i] < lista[j]:
                


def random_list(n):
    lista = list()

    for i in range(0, n):
        temp = random.randint(0, n-1)
        while temp in lista:
            temp = random.randint(0, n-1)

        lista.append(temp)

    return lista


def nearly_sorted(n):
    lista = random_list(10)


