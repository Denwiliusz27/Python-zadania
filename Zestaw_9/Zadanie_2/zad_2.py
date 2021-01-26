"""
ZADANIE 11.3
Poprawić wybrany algorytm sortowania, aby przyjmował jako dodatkowy argument funkcję porównującą elementy na liście
[przykład na wykładzie dla funkcji bubblesort()].
"""

import random


def cmp(a, b):
    return (a > b) - (a < b)


def swap(lista, i, j):
    lista[i], lista[j] = lista[j], lista[i]


def random_list(n):
    lista = list()

    for i in range(0, n):
        temp = random.randint(0, n - 1)
        while temp in lista:
            temp = random.randint(0, n - 1)

        lista.append(temp)

    return lista


def insert_sort(lista, cmp_f=cmp):
    left = 0
    right = len(lista)
    for i in range(left + 1, right):
        for j in range(i, left, -1):
            if cmp_f(lista[j - 1], lista[j]) > 0:
                swap(lista, j - 1, j)
            else:
                break

    return lista


if __name__ == '__main__':
    lista = random_list(10)
    print("Lista do posortowania: ", lista)
    print("Insertsort z cmp: ", insert_sort(lista))
