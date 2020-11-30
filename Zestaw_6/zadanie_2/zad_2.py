import unittest, math


class Frac:
    """Klasa reprezentująca ułamek."""

    def __init__(self, x=0, y=1):
        self.x = x
        self.y = y
        if self.y == 0:
            raise ZeroDivisionError

    def __str__(self):  # zwraca "x/y" lub "x" dla y=1
        return "{}/{}".format(int(self.x), int(self.y))

    def __repr__(self):  # zwraca "Frac(x, y)"
        return "Frac({}, {})".format(int(self.x), int(self.y))

    # Python 2
    # def __cmp__(self, other): pass  # cmp(frac1, frac2)

    # Python 2.7 i Python 3
    def __eq__(self, other):
        x1 = self.x
        x2 = other.x

        if self.y != other.y:
            x1 = self.x * other.y
            x2 = other.x * self.y

        return x1 == x2

#        return self.x / self.y == other.x / other.y

    def __ne__(self, other):
        x1 = self.x
        x2 = other.x

        if self.y != other.y:
            x1 = self.x * other.y
            x2 = other.x * self.y

        return x1 != x2

        # return self.x / self.y != other.x / other.y

    def __lt__(self, other):
        x1 = self.x
        x2 = other.x

        if self.y != other.y:
            x1 = self.x * other.y
            x2 = other.x * self.y

        return x1 < x2
        # return self.x / self.y < other.x / other.y

    def __le__(self, other):
        x1 = self.x
        x2 = other.x

        if self.y != other.y:
            x1 = self.x * other.y
            x2 = other.x * self.y

        return x1 <= x2
        # return self.x / self.y <= other.x / other.y

   # def __gt__(self, other):
      #  x1 = self.x
    #         x2 = other.x
    #
    #         if self.y != other.y:
    #             x1 = self.x * other.y
    #             x2 = other.x * self.y
    #
    #         return x1 > x2

   # def __ge__(self, other):
      #  x1 = self.x
    #         x2 = other.x
    #
    #         if self.y != other.y:
    #             x1 = self.x * other.y
    #             x2 = other.x * self.y
    #
    #         return x1 >= x2

    def __add__(self, other):  # frac1 + frac2
        if self.y != other.y:
            x = self.x * other.y + other.x * self.y
            y = self.y * other.y
        else:
            x = self.x + other.x
            y = self.y

        nwd = math.gcd(x, y)
        return Frac(x / nwd, y / nwd)

    # return uproszczenie(x, y)

    def __sub__(self, other):  # frac1 - frac2
        if self.y != other.y:
            x = self.x * other.y - other.x * self.y
            y = self.y * other.y
        else:
            x = self.x - other.x
            y = self.y

        nwd = math.gcd(x, y)
        return Frac(x / nwd, y / nwd)

    def __mul__(self, other):  # frac1 * frac2
        x = self.x * other.x
        y = self.y * other.y

        nwd = math.gcd(x, y)
        return Frac(x / nwd, y / nwd)

    def __div__(self, other):  # frac1 / frac2, Python 2
        pass

    def __truediv__(self, other):  # frac1 / frac2, Python 3
        x = self.x * other.y
        y = self.y * other.x

        nwd = math.gcd(x, y)
        return Frac(x / nwd, y / nwd)

    def __floordiv__(self, other):  # frac1 // frac2, opcjonalnie
        frac = self / other
        x = frac.x // frac.y
        y = 1
        return Frac(x, 1)

    def __mod__(self, other):  # frac1 % frac2, opcjonalnie
        liczba = self / other
        return int(liczba.x % liczba.y)

    # operatory jednoargumentowe
    def __pos__(self):  # +frac = (+1)*frac
        return self

    def __neg__(self):  # -frac = (-1)*frac
        return Frac(-self.x, self.y)

    def __invert__(self):  # odwrotnosc: ~frac
        return Frac(self.y, self.x)

    def __float__(self):  # float(frac)
        return self.x / self.y

    def __hash__(self):
        return hash(float(self))  # immutable fracs
        # assert set([2]) == set([2.0])


def uproszczenie(x, y):
    dzielnik = 1

    if x > y:
        zakres = y + 1
    else:
        zakres = x + 1
    for i in range(zakres, 1, -1):
        if x % i == 0 and y % i == 0:
            dzielnik = i
            break
    return Frac(x / dzielnik, y / dzielnik)


# Kod testujący moduł.
"""
class TestFrac(unittest.TestCase):

    def setUp(self): pass

    def test_print(self):
        self.assertEqual(Frac(1, 3).__str__(), "1/3")
        self.assertNotEqual(Frac(1, 3).__str__(), "3/1")
        self.assertEqual(Frac(1, 3).__repr__(), "Frac(1, 3)")
        self.assertNotEqual(Frac(1, 3).__repr__(), "Frac(3, 1)")

"""

if __name__ == '__main__':
    # unittest.main()
    f1 = Frac(3, 4)
    f2 = Frac(6, 8)
    print(Frac(2, 4) + Frac(8, 4))
    # print(Frac(3, 0))
    print(f1 / f2)
    print("#####")
    print(f1 // f2)
    print(f1 % f2)
    print(f1 == f2)
    print(f1 > f2)
    print(f1 >= f2)
