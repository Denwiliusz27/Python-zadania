def main():
    ilosc = input("Podaj liczbe nieparzyta: ")
    space = 0


    while (ilosc % 2 == 0) or (ilosc < 0):
        print("Podano niepoprawna liczbe.")
        ilosc = int(input("Podaj ponownie: "))

    while ilosc > 0:
        for j in range(space):
            print(' ', end=""),
        for i in range(ilosc):
            print('*', end="")
        ilosc -= 2
        space += 1
        print()

main()