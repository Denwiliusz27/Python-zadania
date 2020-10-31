def add(lista, element):
    #print("mam tabele: ", lista)
    l_length = 0

    for i in lista:
        if isinstance(i, list):
            #print("wchodze do tabeli: ", i)
            add(lista[lista.index(i)], element)
        else:
            l_length += 1

    if l_length == len(lista):
        lista.append(element)
    return


def longest(lista):
    count = 0

    for i in lista:
        if type(i) == list:
            count += 1
            longest(i)

    return count


def longest_nested_list(lista):
    length = 0
    temp = 0
    index = 0
    #print("wchodze z : ", lista)
    print("indeks = ", temp)

    for i in lista:
        if isinstance(i, list):
            length += 1
            print("mam liste: ", i)
            index = lista.index(i)
            temp += longest_nested_list(i)

        if temp > length:
            length = temp

    return length




def main():
    lista = [1, 2, [3, 4, [5, 6], 5], 3, 4]
    lista1 = [1, [2, 3], 4]
    lista2 = [3, 4, [2, [1, 2, [7, 8], 3, 4], 3, 4], 5, 6, 7]
    amount_of_nested_list = 0
    index = 0
    indeksy = []

    add(lista, 99)
    print(lista)

    add(lista1, 99)
    print(lista1)

    add(lista2, 99)
    print(lista2)

   # print(longest_nested_list(lista))

"""    
    for i in lista:
        if isinstance(i, list):
            amount, indeksy = add(i, indeksy)
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
