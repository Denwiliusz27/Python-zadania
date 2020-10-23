ilosc = int(input("Podaj liczbe nieparzyta: "))

while (ilosc % 2 == 0) or (ilosc < 0):
    print("Podano niepoprawna liczbe.")
    ilosc = int(input("Podaj ponownie: "))

print("Wpisano liczbe: ", ilosc)