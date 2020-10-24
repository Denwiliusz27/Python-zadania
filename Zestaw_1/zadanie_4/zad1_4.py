def is_positive_number(input_string):
    liczba = input_string

    while not (liczba.isnumeric()):
        print()
        liczba = input("Niepoprawne dane, wpisz ponownie: ")

    return liczba


def main():
    y = input("\nPodaj liczbe wierszy: ")
    y = int(is_positive_number(y))

    while y == 0:
        y = input("\nPodano zerowa liczbe wierszy. Wpisz ponownie: ")
        y = int(is_positive_number(y))

    x = input("\nPodaj liczbe kolumn: ")
    x = int(is_positive_number(x))

    while x == 0:
        x = input("\nPodano zerowa liczbe kolumn. Wpisz ponownie: ")
        x = int(is_positive_number(x))

    tabela = '+'

    for i in range(0, y + 1):
        for j in range(0, x):
            tabela += "---+"
        tabela += '\n'
        if i < y:
            tabela += '|'
            for n in range(0, x):
                tabela += '   |'
            tabela += '\n+'

    print("\nTabela ", y, "x", x, " :")
    print(tabela)


if __name__ == '__main__':
    main()
