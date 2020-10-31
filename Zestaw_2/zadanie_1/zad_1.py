def iteracja(lista, element):
    print("mam tabele: ", lista)
    l_length = 0

    for i in lista:
        if isinstance(i, list):
            print("wchodze do tabeli: ", i)
            iteracja(lista[lista.index(i)], element)
        else:
            l_length += 1

    if l_length == len(lista):
        lista.append(element)
    return


def add(lista, element):
    for i in lista:
        if isinstance(i, list):
            print("wchodze do tabeli: ", i)
            add(i, element)
        else:
            print("chce dodac")
            lista.append(element)


def main():
    # lista = [1, 2, [3, 4, [5, 6], 5], 3, [2, [3, [4, 6]]], 4]
    lista = [1, 2, [3, 4, [5, 6], 5], 3, 4]
    amount_of_nested_list = 0
    index = 0
    indeksy = []

    iteracja(lista, 99)
    print(lista)

"""    
    for i in lista:
        if isinstance(i, list):
            amount, indeksy = iteracja(i, indeksy)
            if amount > amount_of_nested_list:
                amount_of_nested_list = amount
                index = lista.index(i)

    indeksy.append(index)

    print(amount_of_nested_list)
    print(indeksy)

    #add(lista[index], 101)
    print(lista)
"""

main()
