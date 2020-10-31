def main():
    lancuch = input("Wpisz lancuch znkow: ")
    ilosc_slow = 0
    ilosc_liter = 0
    dlugosc_slowa = 0
    lista_znakow = list()
    czestosc_wystepowania = list()

    for znak in lancuch:
        print("Mam: ", znak)

        if (64 < ord(znak) < 91) or (96 < ord(znak) < 123):
            ilosc_liter += 1
            dlugosc_slowa += 1
            print("ilosc_liter: ", ilosc_liter)
            print("dlugosc_slowa: ", dlugosc_slowa)

            if znak not in lista_znakow:
                lista_znakow.append(znak)

        elif ord(znak) == 32:
            ilosc_slow += 1
            dlugosc_slowa = 0
            print("ilosc_slow: ", ilosc_slow)

    ilosc_slow += 1

    for znak in lista_znakow:
        czestosc_wystepowania.append([znak, 0])

    for znak in lancuch:
        for para in czestosc_wystepowania:
            if ord(znak) == ord(para[0]):
                para[1] += 1

    print("~~~~~~~~~~~~~~")
    print("ilosc_slow: ", ilosc_slow)
    print("ilosc_liter: ", ilosc_liter)
    print(lista_znakow)
    print(czestosc_wystepowania)


if __name__ == '__main__':
    main()
