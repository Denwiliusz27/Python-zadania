import random


def swap(lista, i, j):
    lista[i], lista[j] = lista[j], lista[i]


def insert_sort(lista):
    print("lista: ", end="")
    print(lista)
    for i in range(1, len(lista)):
        for j in range(i, 0, -1):
            if lista[j] < lista[j - 1]:
                swap(lista, j - 1, j)

    return lista


def bubblesort(lista):
    for i in range(0, len(lista)):
        for j in range(0, len(lista)):
            if lista[j] > lista[j + 1]:
                swap(lista, j + 1, j)


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

    print(len(lista))
    print(lista)
    ile_zmian = len(lista)//3
    print("ile zmian = ", ile_zmian)

    indeksy = list()
    for i in range(ile_zmian):
        temp = random.randint(1, len(lista)-1)
        while temp in indeksy:
            temp = random.randint(1, len(lista)-1)
        indeksy.append(temp)

    print("po dodaniu")
    print(indeksy)
    for i in range(len(indeksy)):
        print("i=" + str(i))
        print("indeksy[i]=" + str(indeksy[i]))
        swap(lista, indeksy[i], indeksy[i]-1)
        print(lista)

    return lista
