letters = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}

# słownik alternatywny
letters_v2 = dict([
    ("I", 1),
    ("V", 5),
    ("X", 10),
    ("L", 50),
    ("C", 100),
    ("D", 500),
    ("M", 1000)
])


def roman2int(liczba):
    suma = 0
    pos = len(liczba) - 1

    while pos >= 0:
        letter = liczba[pos]

        if pos < len(liczba) - 1:
            if letters[letter] < letters[liczba[pos + 1]]:
                suma -= letters[letter]
            elif letters[letter] >= letters[liczba[pos + 1]]:
                suma += letters[letter]
        else:
            suma += letters[letter]
        pos -= 1

    return suma


if __name__ == '__main__':
    liczba = "MMCCCLXXVII"
    print(liczba, " =", roman2int(liczba))
