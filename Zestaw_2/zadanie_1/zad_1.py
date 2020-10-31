def iteracja(lista, indeksy):
    index = 1
    print("mam tabele: ", lista)

    for i in lista:
        if isinstance(i, list):
            indeksy.append(lista.index(i))
            print("index: ", index)
            print("wchodze do tabeli: ", i)
            index += 1
            iteracja(i, indeksy)

    print("indeks na koncu: ", index)
    return index, indeksy


def add(lista, element):
    for i in lista:
        if isinstance(i, list):
            print("wchodze do tabeli: ", i)
            add(i, element)
        else:
            print("chce dodac")
            lista.append(element)


def main():
    #lista = [1, 2, [3, 4, [5, 6], 5], 3, [2, [3, [4, 6]]], 4]
    lista = [1, 2, [3, 4, [5, 6], 5], 3, 4]
    amount_of_nested_list = 0
    index = 0
    indeksy = []

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


main()
