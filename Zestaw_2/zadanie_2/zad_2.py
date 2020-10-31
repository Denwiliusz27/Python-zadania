def is_positive_number(input_string):
    liczba = input_string

    while not (liczba.isnumeric()):
        print()
        liczba = input("Niepoprawne dane, wpisz ponownie: ")

    liczba = int(liczba)

    while liczba < 1900 or liczba > 100000:
        liczba = input("\nLiczba nie nalezy do zakresu, wpisz ponownie: ")
        liczba = int(is_positive_number(liczba))
        break

    return int(liczba)


def main():
    rok = input("Podaj rok z zakresu 1900 - 100000: ")
    rok = is_positive_number(rok)

    print()

    if rok % 4 != 0:
        print(False)
    else:
        if rok % 100 == 0:
            if rok % 400 == 0:
                print(True)
            else:
                print(False)
        else:
            print(True)


if __name__ == '__main__':
    main()