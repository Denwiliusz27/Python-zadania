def is_positive_number(input_string):
    liczba = input_string

    while not (liczba.isnumeric()):
        print()
        liczba = input("Niepoprawne dane, wpisz ponownie: ")

    return liczba


def main():
    dlugosc = input("\nPodaj dlugosc miarki: ")
    dlugosc = int(is_positive_number(dlugosc))
    miarka = '|'

    for odcinek in range(dlugosc):
        for kropka in range(4):
            miarka += '.'
        miarka += '|'

    miarka += '\n'

    for i in range(dlugosc + 1):
        miarka += str(i)
        if i >= 99:
            miarka += "  "
        elif i >= 9:
            miarka += "   "
        else:
            miarka += "    "

    print(miarka)


main()