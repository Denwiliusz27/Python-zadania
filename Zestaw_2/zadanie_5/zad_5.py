def is_positive_number(input_string):
    liczba = input_string

    while not (liczba.isnumeric()) or int(liczba) == 0 or int(liczba) > 2147483647:
        print()
        liczba = input("Niepoprawne dane, wpisz ponownie: ")

    return liczba


def fun(N):
    liczba = ""
    dl_przerwy = 0
    temp = 0

    while N != 0:
        if N % 2 == 0:
            liczba = "0" + liczba
        else:
            liczba = "1" + liczba
        N = N // 2

    print("\nLiczba = ", liczba)

    for znak in liczba:
        if znak == "0":
            temp += 1
        elif znak == "1" and temp > 0:
            if temp > dl_przerwy:
                dl_przerwy = temp
            temp = 0

    return dl_przerwy


def main():
    liczba = input("Podaj liczbe w systemie dziesietnym z przedzialu [1, 2147483647]: ")
    liczba = int(is_positive_number(liczba))

    print("Dlugosc najdluzszej binarnej pzrerwy: ", fun(liczba))


if __name__ == '__main__':
    main()
