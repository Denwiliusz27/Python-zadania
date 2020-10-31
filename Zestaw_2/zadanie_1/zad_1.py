def add(lista, element):
    l_length = 0

    for i in lista:
        if isinstance(i, list):
            add(lista[lista.index(i)], element)
        else:
            l_length += 1

    if l_length == len(lista):
        lista.append(element)

    return


def main():
    lista = [1, 2, [3, 4, [5, 6], 5], 3, 4]
    lista1 = [1, [2, 3], 4]
    lista2 = [3, 4, [2, [1, 2, [7, 8], 3, 4], 3, 4], 5, 6, 7]

    add(lista, 99)
    print(lista)

    add(lista1, 99)
    print(lista1)

    add(lista2, 99)
    print(lista2)


if __name__ == '__main__':
    main()
