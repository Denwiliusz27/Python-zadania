class Frac:
    """Klasa reprezentująca ułamek."""

    def __init__(self, x=0, y=1):
        self.x = x
        self.y = y

    def __str__(self):  # zwraca "x/y" lub "x" dla y=1
        if self.y == 1:
            return "{}".format(self.y)
        else:
            return "{}/{}".format(self.x, self.y)

    def __repr__(self):  # zwraca "Frac(x, y)"
        return "Frac({}, {})".format(self.x, self.y)

    # Python 2
    # def __cmp__(self, other): pass  # cmp(frac1, frac2)

    # Python 2.7 i Python 3
    def __eq__(self, other):
        return self.x / self.y == other.x / other.y

    def __ne__(self, other):
        return not (self.x / self.y == other.x / other.y)

    def __lt__(self, other):
        return self.x / self.y < other.x / other.y

    def __le__(self, other):
        return self.x / self.y <= other.x / other.y

    def __gt__(self, other):
        return self.x / self.y > other.x / other.y

    def __ge__(self, other):
        return self.x / self.y >= other.x / other.y

    def __add__(self, other):  # frac1 + frac2
        # return self.x/self.y + other.x/other.y
        if self.y != other.y:
            x = self.x * other.y + other.x * self.y
            y = self.y * other.y

            dzielnik = 1
            for i in range(x + 1, 0, -1):
                if x % i == 0 and y % i == 0:
                    dzielnik = i
                    break

            return Frac(x / dzielnik, y / dzielnik)
        else:
            return Frac(self.x + other.x, self.y)

    def __sub__(self, other):
        pass  # frac1 - frac2

    def __mul__(self, other):
        pass  # frac1 * frac2

    def __div__(self, other):
        pass  # frac1 / frac2, Python 2

    def __truediv__(self, other):
        pass  # frac1 / frac2, Python 3

    def __floordiv__(self, other):
        pass  # frac1 // frac2, opcjonalnie

    def __mod__(self, other):
        pass  # frac1 % frac2, opcjonalnie

    # operatory jednoargumentowe
    def __pos__(self):  # +frac = (+1)*frac
        return self

    def __neg__(self):  # -frac = (-1)*frac
        return Frac(-self.x, self.y)

    def __invert__(self):  # odwrotnosc: ~frac
        return Frac(self.y, self.x)

    def __float__(self):
        pass  # float(frac)

    def __hash__(self):
        return hash(float(self))  # immutable fracs
        # assert set([2]) == set([2.0])


# Kod testujący moduł.

# import unittest

# class TestFrac(unittest.TestCase): pass

def fun(x1, y1, x2, y2):
    x = x1 * y2 + x2 * y1
    y = y1 * y2

    dzielnik = 1
    for i in range(x + 1, 0, -1):
        print("sprawdzam ", i)
        if x % i == 0 and y % i == 0:
            dzielnik = i
            break

    print(x / dzielnik, "/", y / dzielnik)


if __name__ == '__main__':
    u1 = Frac(7, 36)
    u2 = Frac(8, 36)
    print(u1.x / u1.y)
    print(u2.x / u2.y)
    print(u1 == u2)
    print(u1 + u2)
