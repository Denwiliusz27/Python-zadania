letters = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}


def roman2int(liczba):
    suma = 0
    letter = 0

    while letter < len(liczba):
        print(letter, end=": ")
        if letter < len(liczba)-1:
            if letters[liczba[letter]] < letters[liczba[letter+1]]:
                print(liczba[letter], " < ", liczba[letter+1])
                suma -= letters[liczba[letter]] - letters[liczba[letter+1]]
                letter += 1
            elif letters[liczba[letter]] > letters[liczba[letter+1]]:
                print(liczba[letter], " > ", liczba[letter+1])
                suma += letters[liczba[letter+1]] + letters[liczba[letter]]
                letter += 1
            else:
                print(liczba[letter], " = ", liczba[letter+1])
                suma += letters[liczba[letter]]
        else:
            print("inny")
            suma += letters[liczba[letter]]
        letter += 1
        print(suma)

    return suma


if __name__ == '__main__':
    print(roman2int("DLXXI"))
