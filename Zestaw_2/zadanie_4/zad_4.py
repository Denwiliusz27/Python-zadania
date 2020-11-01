def is_positive_number(input_string):
    liczba = input_string

    while not (liczba.isnumeric()) or int(liczba) == 0:
        print()
        liczba = input("Niepoprawne dane, wpisz ponownie: ")

    return liczba


def main():
    x = input("Podaj parametr x: ")
    x = int(is_positive_number(x))

    y = input("Podaj parametr y: ")
    y = int(is_positive_number(y))

    z = input("Podaj parametr z: ")
    z = int(is_positive_number(z))

    n = input("Podaj parametr n: ")
    n = int(is_positive_number(n))

    lista = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n]

    print("\nLista mozliwych kombinacji i, j oraz k:")
    print(lista)



if __name__ == '__main__':
    main()
