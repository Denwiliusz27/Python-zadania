import random
import numpy


def swap(lista, i, j):
    lista[i], lista[j] = lista[j], lista[i]


def insert_sort(lista):
    for i in range(1, len(lista)):
        for j in range(i, 0, -1):
            if lista[j] < lista[j - 1]:
                swap(lista, j - 1, j)

    return lista


def insert_sort_reverse(lista):
    for i in range(1, len(lista)):
        for j in range(i, 0, -1):
            if lista[j] > lista[j - 1]:
                swap(lista, j - 1, j)

    return lista


def random_list(n):
    lista = list()

    for i in range(0, n):
        temp = random.randint(0, n - 1)
        while temp in lista:
            temp = random.randint(0, n - 1)

        lista.append(temp)

    return lista


def nearly_sorted(n):
    lista = insert_sort(random_list(n))

    ile_zmian = len(lista) // 3

    indeksy = list()
    for i in range(ile_zmian):
        temp = random.randint(1, len(lista) - 1)
        while temp in indeksy:
            temp = random.randint(1, len(lista) - 1)
        indeksy.append(temp)

    for i in range(len(indeksy)):
        swap(lista, indeksy[i], indeksy[i] - 1)

    return lista


def nearly_sorted_reverse(n):
    lista = insert_sort_reverse(random_list(n))

    ile_zmian = len(lista) // 3

    indeksy = list()
    for i in range(ile_zmian):
        temp = random.randint(1, len(lista) - 1)
        while temp in indeksy:
            temp = random.randint(1, len(lista) - 1)
        indeksy.append(temp)

    for i in range(len(indeksy)):
        swap(lista, indeksy[i], indeksy[i] - 1)

    return lista


def random_gauss(n):
    mu, sigma = 1, 0.005
    lista = numpy.random.normal(mu, sigma, n)
    return lista


def list_with_repeats(n):
    number = random.randint(1, n-1)
    k = random_list(number)

    lista = list()
    for i in range(n):
        temp = k[random.randint(0, len(k)-1)]
        while temp in lista:
            if i < len(k):
                temp = k[random.randint(0, len(k)-1)]
            else:
                break
        lista.append(temp)

    return lista


