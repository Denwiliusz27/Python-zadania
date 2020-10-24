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
    liczby = ''

    for odcinek in range(dlugosc):
        for kropka in range(4):
            miarka += '.'
        miarka += '|'

    for i in range(dlugosc+1):
        liczby += str(i)
        if i >= 9:
            liczby += "   "
        else:
            liczby += "    "

    print(miarka)
    print(liczby)

main()
