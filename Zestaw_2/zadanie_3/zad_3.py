def main():
    lancuch = input("Wpisz lancuch znakow: ")
    ilosc_slow = 0
    ilosc_liter = 0
    dlugosc_slowa = 0
    lista_znakow = list()
    czestosc_wystepowania = list()

    for znak in lancuch:
        if (64 < ord(znak) < 91) or (96 < ord(znak) < 123):
            ilosc_liter += 1
            dlugosc_slowa += 1

            if znak not in lista_znakow:
                lista_znakow.append(znak)

        elif ord(znak) == 32:
            ilosc_slow += 1
            dlugosc_slowa = 0

    ilosc_slow += 1

    for znak in lista_znakow:
        czestosc_wystepowania.append([znak, 0])

    for znak in lancuch:
        for para in czestosc_wystepowania:
            if ord(znak) == ord(para[0]):
                para[1] += 1

    print("\nIlosc slow: ", ilosc_slow)
    print("Ilosc liter: ", ilosc_liter)

    print("\nCzestosc wystepowania liter:")
    for para in czestosc_wystepowania:
        print(para[0], ": ", para[1])


if __name__ == '__main__':
    main()
