def is_positive_number(input_string):
    liczba = input_string

    while not (liczba.isnumeric()):
        print()
        liczba = input("Niepoprawne dane, wpisz ponownie: ")

    return liczba


def main():
    y = input("\nPodaj liczbe wierszy: ")
    y = int(is_positive_number(y))

    x = input("\nPodaj liczbe kolumn: ")
    x = int(is_positive_number(x))

    if (x > 0) and (y > 0):
        tabela = '+'
    else:
        return

    for i in range(1, y):
        for j in range(1, x):
            tabela += "---+"
        tabela += '\n'
        if i < y:
            tabela += '|'
            for n in range(1, x):
                tabela += '   |'
            tabela += '\n+'

    print(tabela)


if __name__ == '__main__':
    main()
