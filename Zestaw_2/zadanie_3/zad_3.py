def main():
    lancuch = input("Wpisz lancuch znkow: ")
    ilosc_slow = 0
    ilosc_liter = 0
    dlugosc_slowa = 0
    lista = list()

    for znak in lancuch:
        print("Mam: ", znak, " o kodzie: ", ord(znak))

        if (64 < ord(znak) < 91) or (96 < ord(znak) < 123):
            ilosc_liter += 1
            dlugosc_slowa += 1
            print("ilosc_liter: ", ilosc_liter)
            print("dlugosc_slowa: ", dlugosc_slowa)
            if znak not in list:
                list1 = [znak, 1]
                lista.append(list1)
            else:
                for i in lista:
                    if i[0]


        elif ord(znak) == 32:
            ilosc_slow += 1
            dlugosc_slowa = 0
            print("ilosc_slow: ", ilosc_slow)

    ilosc_slow += 1
    dlugosc_slowa = 0

    print("~~~~~~~~~~~~~~")
    print("ilosc_slow: ", ilosc_slow)
    print("ilosc_liter: ", ilosc_liter)


if __name__ == '__main__':
    main()
