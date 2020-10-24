def is_number(input_string):
    liczba = input_string

    while not (liczba.isnumeric()):
        print()
        liczba = input("Niepoprawne dane, wpisz ponownie: ")

    return liczba


def main():
    ilosc = input("Podaj liczbe nieparzyta dodatnia: ")
    space = 0

    ilosc = int(is_number(ilosc))

    while ilosc % 2 == 0:
        print()
        ilosc = input("Podana liczba nie jest nieparzysta, podaj ponownie: ")
        ilosc = int(is_number(ilosc))

    print("\nWpisano liczbe: " + str(ilosc) + "\n")
    while ilosc > 0:
        for j in range(space):
            print(' ', end=""),
        for i in range(ilosc):
            print('*', end="")
        ilosc -= 2
        space += 1
        print()


main()
