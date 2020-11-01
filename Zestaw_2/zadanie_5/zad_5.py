def is_positive_number(input_string):
    liczba = input_string

    while not (liczba.isnumeric()) or int(liczba) == 0:
        print()
        liczba = input("Niepoprawne dane, wpisz ponownie: ")

    return liczba


def fun(N):
    liczba = ""

    for i in bin(N)[2:]:
        liczba += i

    

    return liczba


def main():
    liczba = input("Podaj liczbe w systemie dziesietnym z przedzialu [1, 2147483647]: ")
    liczba = int(is_positive_number(liczba))

    liczba1 = fun(liczba)
    print(liczba1)


if __name__ == '__main__':
    main()
