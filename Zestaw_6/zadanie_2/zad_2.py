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
        if self.y == other.y:
            x = self.x * other.y + other.x * self.y
            y = self.y * other.y
        else:
            x = self.x + other.x
            y = self.y

        return uproszczenie(x, y)

    def __sub__(self, other):  # frac1 - frac2
        if self.y == other.y:
            x = self.x * other.y - other.x * self.y
            y = self.y * other.y
        else:
            x = self.x - other.x
            y = self.y

        return uproszczenie(x, y)

    def __mul__(self, other):  # frac1 * frac2
        x = self.x * other.x
        y = self.y * other.y

        return uproszczenie(x, y)

    def __div__(self, other):  # frac1 / frac2, Python 2
        pass

    def __truediv__(self, other):  # frac1 / frac2, Python 3
        x = self.x * other.y
        y = self.y * other.x

        return uproszczenie(x, y)

    def __floordiv__(self, other):  # frac1 // frac2, opcjonalnie
        frac = self / other

        if frac.x < frac.y:
            return Frac(0, 1)
        elif frac.x == frac.y:
            return Frac(1, 1)
        else:  # x > y
            while frac.x % frac.y != 0:
                frac.x -= 1
            return uproszczenie(frac.x, frac.y)

    def __mod__(self, other):
        pass  # frac1 % frac2, opcjonalnie

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



# Kod testujący moduł.

# import unittest

# class TestFrac(unittest.TestCase): pass

if __name__ == '__main__':
    u1 = Frac(3, 7)
    u2 = Frac(1, 3)
    print(u1.x / u1.y)
    print(u2.x / u2.y)
    print(u1 == u2)
    print(u1 + u2)
    print(4 // 6)
