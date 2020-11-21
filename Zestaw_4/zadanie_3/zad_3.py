def sumowanie(lista):
    wyniki = []
    for elem in lista:
        suma = 0
        for i in elem:
            if not isinstance(i, str):
                suma += i
        wyniki.append(suma)
    return wyniki


if __name__ == '__main__':
    lista = [[], ["ala"], [3], (1, 2.3, 'a'), [3, 4], (5, 6, 7)]
    print("Suma elementów = ", sumowanie(lista))
