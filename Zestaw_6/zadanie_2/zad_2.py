import unittest, math


class Frac:
    """Klasa reprezentująca ułamek."""

    def __init__(self, x=0, y=1):
        self.x = x
        self.y = y

    def __str__(self):  # zwraca "x/y" lub "x" dla y=1
        if self.y == 1:
            return "{}".format(int(self.x))
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

    def __lt__(self, other):  # <
        x1 = self.x
        x2 = other.x

        if self.y != other.y:
            x1 = self.x * other.y
            x2 = other.x * self.y

        return x1 < x2

    def __le__(self, other):  # <=
        x1 = self.x
        x2 = other.x

        if self.y != other.y:
            x1 = self.x * other.y
            x2 = other.x * self.y

        return x1 <= x2

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
        return int(x)

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

class TestFrac(unittest.TestCase):

    def setUp(self):
        self.f1 = Frac(3, 6)
        self.f2 = Frac(5, 17)
        self.f3 = Frac(2, 1)
        self.f4 = Frac(4, 4)
        self.f5 = Frac(0, 3)

    def test_init(self):
        self.assertEqual(self.f1.x, 3)
        self.assertEqual(self.f1.y, 6)

        self.assertEqual(self.f2.x, 5)
        self.assertEqual(self.f2.y, 17)

        self.assertEqual(self.f3.x, 2)
        self.assertEqual(self.f3.y, 1)

        self.assertEqual(self.f4.x, 4)
        self.assertEqual(self.f4.y, 4)

        self.assertEqual(self.f5.x, 0)
        self.assertEqual(self.f5.y, 3)

    def test_print(self):
        self.assertEqual(self.f1.__str__(), "3/6")
        self.assertEqual(self.f1.__repr__(), "Frac(3, 6)")

        self.assertEqual(self.f2.__str__(), "5/17")
        self.assertEqual(self.f2.__repr__(), "Frac(5, 17)")

        self.assertEqual(self.f3.__str__(), "2")
        self.assertEqual(self.f3.__repr__(), "Frac(2, 1)")

        self.assertEqual(self.f4.__str__(), "4/4")
        self.assertEqual(self.f4.__repr__(), "Frac(4, 4)")

        self.assertEqual(self.f5.__str__(), "0/3")
        self.assertEqual(self.f5.__repr__(), "Frac(0, 3)")

    def test_eq(self):
        self.assertTrue(self.f1 == Frac(3, 6))
        self.assertTrue(self.f1 == Frac(1, 2))
        self.assertFalse(self.f1 == Frac(6, 3))

        self.assertTrue(self.f2 == Frac(5, 17))
        self.assertTrue(self.f2 == Frac(10, 34))
        self.assertFalse(self.f2 == Frac(17, 5))

        self.assertTrue(self.f3 == Frac(2, 1))
        self.assertTrue(self.f3 == Frac(4, 2))
        self.assertFalse(self.f3 == Frac(1, 2))

        self.assertTrue(self.f4 == Frac(4, 4))
        self.assertTrue(self.f4 == Frac(3, 3))
        self.assertFalse(self.f4 == Frac(2, 1))

        self.assertTrue(self.f5 == Frac(0, 3))
        self.assertTrue(self.f5 == Frac(0, 7))
        self.assertFalse(self.f5 == Frac(1, 3))

    def test_ne(self):
        self.assertFalse(self.f1 != Frac(3, 6))
        self.assertTrue(self.f1 != Frac(6, 3))
        self.assertTrue(self.f1 != Frac(12, 6))

        self.assertFalse(self.f2 != Frac(5, 17))
        self.assertTrue(self.f2 != Frac(17, 5))
        self.assertTrue(self.f2 != Frac(51, 15))

        self.assertFalse(self.f3 != Frac(2, 1))
        self.assertTrue(self.f3 != Frac(1, 2))
        self.assertTrue(self.f3 != Frac(2, 4))

        self.assertFalse(self.f4 != Frac(4, 4))
        self.assertTrue(self.f4 != Frac(2, 1))
        self.assertTrue(self.f4 != Frac(6, 3))

        self.assertFalse(self.f5 != Frac(0, 3))
        self.assertTrue(self.f5 != Frac(1, 3))
        self.assertTrue(self.f5 != Frac(3, 9))

    def test_lt(self):
        self.assertTrue(self.f1 < Frac(4, 6))
        self.assertTrue(self.f1 < Frac(3, 5))
        self.assertFalse(self.f1 < Frac(1, 2))
        self.assertFalse(self.f1 < Frac(2, 5))

        self.assertTrue(self.f2 < Frac(6, 17))
        self.assertTrue(self.f2 < Frac(11, 20))
        self.assertFalse(self.f2 < Frac(5, 17))
        self.assertFalse(self.f2 < Frac(3, 19))

        self.assertTrue(self.f3 < Frac(3, 1))
        self.assertTrue(self.f3 < Frac(5, 2))
        self.assertFalse(self.f3 < Frac(1, 1))
        self.assertFalse(self.f3 < Frac(8, 5))

        self.assertTrue(self.f4 < Frac(5, 4))
        self.assertTrue(self.f4 < Frac(9, 7))
        self.assertFalse(self.f4 < Frac(1, 1))
        self.assertFalse(self.f4 < Frac(7, 8))

        self.assertTrue(self.f5 < Frac(1, 3))
        self.assertTrue(self.f5 < Frac(3, 7))
        self.assertFalse(self.f5 < Frac(0, 2))
        self.assertFalse(self.f5 < Frac(-1, 4))

    def test_le(self):
        self.assertTrue(self.f1 <= Frac(3, 6))
        self.assertTrue(self.f1 <= Frac(4, 6))
        self.assertTrue(self.f1 <= Frac(7, 9))
        self.assertFalse(self.f1 <= Frac(2, 6))
        self.assertFalse(self.f1 <= Frac(3, 7))

        self.assertTrue(self.f2 <= Frac(5, 17))
        self.assertTrue(self.f2 <= Frac(6, 17))
        self.assertTrue(self.f2 <= Frac(10, 20))
        self.assertFalse(self.f2 <= Frac(4, 17))
        self.assertFalse(self.f2 <= Frac(7, 25))

        self.assertTrue(self.f3 <= Frac(2, 1))
        self.assertTrue(self.f3 <= Frac(3, 1))
        self.assertTrue(self.f3 <= Frac(5, 2))
        self.assertFalse(self.f3 <= Frac(1, 1))
        self.assertFalse(self.f3 <= Frac(2, 3))

        self.assertTrue(self.f4 <= Frac(4, 4))
        self.assertTrue(self.f4 <= Frac(1, 1))
        self.assertTrue(self.f4 <= Frac(8, 7))
        self.assertFalse(self.f4 <= Frac(1, 3))
        self.assertFalse(self.f4 <= Frac(1, 3))

        self.assertTrue(self.f5 <= Frac(0, 3))
        self.assertTrue(self.f5 <= Frac(0, 1))
        self.assertTrue(self.f5 <= Frac(3, 8))
        self.assertFalse(self.f5 <= Frac(-1, 3))
        self.assertFalse(self.f5 <= Frac(-3, 20))

    def test_gt(self):
        self.assertTrue(self.f1 > Frac(2, 6))
        self.assertTrue(self.f1 > Frac(1, 3))
        self.assertFalse(self.f1 > Frac(1, 2))
        self.assertFalse(self.f1 > Frac(3, 6))

        self.assertTrue(self.f2 > Frac(4, 17))
        self.assertTrue(self.f2 > Frac(6, 21))
        self.assertFalse(self.f2 > Frac(5, 17))
        self.assertFalse(self.f2 > Frac(11, 15))

        self.assertTrue(self.f3 > Frac(1, 1))
        self.assertTrue(self.f3 > Frac(3, 2))
        self.assertFalse(self.f3 > Frac(3, 1))
        self.assertFalse(self.f3 > Frac(7, 3))

        self.assertTrue(self.f4 > Frac(3, 4))
        self.assertTrue(self.f4 > Frac(5, 7))
        self.assertFalse(self.f4 > Frac(1, 1))
        self.assertFalse(self.f4 > Frac(5, 3))

        self.assertTrue(self.f5 > Frac(-1, 3))
        self.assertTrue(self.f5 > Frac(-3, 12))
        self.assertFalse(self.f5 > Frac(0, 2))
        self.assertFalse(self.f5 > Frac(1, 6))

    def test_ge(self):
        self.assertTrue(self.f1 >= Frac(3, 6))
        self.assertTrue(self.f1 >= Frac(2, 6))
        self.assertTrue(self.f1 >= Frac(3, 8))
        self.assertFalse(self.f1 >= Frac(4, 6))
        self.assertFalse(self.f1 >= Frac(5, 7))

        self.assertTrue(self.f2 >= Frac(5, 17))
        self.assertTrue(self.f2 >= Frac(9, 34))
        self.assertTrue(self.f2 >= Frac(7, 24))
        self.assertFalse(self.f2 >= Frac(6, 17))
        self.assertFalse(self.f2 >= Frac(6, 20))

        self.assertTrue(self.f3 >= Frac(2, 1))
        self.assertTrue(self.f3 >= Frac(2, 2))
        self.assertTrue(self.f3 >= Frac(1, 1))
        self.assertFalse(self.f3 >= Frac(3, 1))
        self.assertFalse(self.f3 >= Frac(9, 4))

        self.assertTrue(self.f4 >= Frac(4, 4))
        self.assertTrue(self.f4 >= Frac(1, 1))
        self.assertTrue(self.f4 >= Frac(3, 4))
        self.assertFalse(self.f4 >= Frac(5, 4))
        self.assertFalse(self.f4 >= Frac(7, 3))

        self.assertTrue(self.f5 >= Frac(0, 3))
        self.assertTrue(self.f5 >= Frac(0, 1))
        self.assertTrue(self.f5 >= Frac(-1, 3))
        self.assertFalse(self.f5 >= Frac(1, 3))
        self.assertFalse(self.f5 >= Frac(3, 8))

    def test_add(self):
        self.assertEqual(self.f1 + Frac(2, 6), Frac(5, 6))
        self.assertEqual(self.f1 + Frac(2, 5), Frac(9, 10))
        self.assertEqual(self.f1 + Frac(2, 5), Frac(27, 30))

        self.assertEqual(self.f2 + Frac(3, 17), Frac(8, 17))
        self.assertEqual(self.f2 + Frac(1, 2), Frac(27, 34))
        self.assertEqual(self.f2 + Frac(1, 2), Frac(54, 68))

        self.assertEqual(self.f3 + Frac(3, 1), Frac(5, 1))
        self.assertEqual(self.f3 + Frac(2, 5), Frac(12, 5))
        self.assertEqual(self.f3 + Frac(2, 5), Frac(24, 10))

        self.assertEqual(self.f4 + Frac(3, 4), Frac(7, 4))
        self.assertEqual(self.f4 + Frac(2, 5), Frac(7, 5))
        self.assertEqual(self.f4 + Frac(2, 5), Frac(21, 15))

        self.assertEqual(self.f5 + Frac(4, 3), Frac(4, 3))
        self.assertEqual(self.f5 + Frac(2, 6), Frac(1, 3))
        self.assertEqual(self.f5 + Frac(2, 6), Frac(3, 9))

    def test_sub(self):
        self.assertEqual(self.f1 - Frac(2, 6), Frac(1, 6))
        self.assertEqual(self.f1 - Frac(2, 5), Frac(1, 10))
        self.assertEqual(self.f1 - Frac(2, 5), Frac(3, 30))

        self.assertEqual(self.f2 - Frac(3, 17), Frac(2, 17))
        self.assertEqual(self.f2 - Frac(1, 2), Frac(-7, 34))
        self.assertEqual(self.f2 - Frac(1, 2), Frac(-14, 68))

        self.assertEqual(self.f3 - Frac(3, 1), Frac(-1, 1))
        self.assertEqual(self.f3 - Frac(2, 5), Frac(8, 5))
        self.assertEqual(self.f3 - Frac(2, 5), Frac(24, 15))

        self.assertEqual(self.f4 - Frac(3, 4), Frac(1, 4))
        self.assertEqual(self.f4 - Frac(2, 5), Frac(3, 5))
        self.assertEqual(self.f4 - Frac(2, 5), Frac(6, 10))

        self.assertEqual(self.f5 - Frac(4, 3), Frac(-4, 3))
        self.assertEqual(self.f5 - Frac(2, 6), Frac(-1, 3))
        self.assertEqual(self.f5 - Frac(2, 6), Frac(-2, 6))

    def test_mul(self):
        self.assertEqual(self.f1 * Frac(2, 5), Frac(1, 5))

        self.assertEqual(self.f2 * Frac(3, 4), Frac(15, 68))

        self.assertEqual(self.f3 * Frac(3, 8), Frac(3, 4))

        self.assertEqual(self.f4 * Frac(3, 7), Frac(3, 7))

        self.assertEqual(self.f5 * Frac(4, 5), Frac(0, 2))

    def test_truediv(self):
        self.assertEqual(self.f1 / Frac(2, 7), Frac(7, 4))

        self.assertEqual(self.f2 / Frac(3, 4), Frac(20, 51))

        self.assertEqual(self.f3 / Frac(3, 5), Frac(10, 3))

        self.assertEqual(self.f4 / Frac(2, 5), Frac(5, 2))

        self.assertEqual(self.f5 / Frac(3, 4), Frac(0, 2))

    def test_floordiv(self):
        self.assertEqual(self.f1 // Frac(2, 7), 1)

        self.assertEqual(self.f2 // Frac(3, 4), 0)

        self.assertEqual(self.f3 // Frac(3, 5), 3)

        self.assertEqual(self.f4 // Frac(2, 5), 2)

        self.assertEqual(self.f5 // Frac(3, 4), 0)

    def test_mood(self):
        self.assertEqual(self.f1 % Frac(2, 7), 3)

        self.assertEqual(self.f2 % Frac(3, 4), 20)

        self.assertEqual(self.f3 % Frac(3, 5), 1)

        self.assertEqual(self.f4 % Frac(2, 5), 1)

        self.assertEqual(self.f5 % Frac(3, 4), 0)

    def test_pos(self):
        self.assertEqual(self.f1, Frac(6, 12))
        self.assertEqual(self.f1, Frac(3, 6))

        self.assertEqual(self.f2, Frac(5, 17))
        self.assertEqual(self.f2, Frac(15, 51))

        self.assertEqual(self.f3, Frac(2, 1))
        self.assertEqual(self.f3, Frac(6, 3))

        self.assertEqual(self.f4, Frac(1, 1))
        self.assertEqual(self.f4, Frac(4, 4))

        self.assertEqual(self.f5, Frac(0, 3))
        self.assertEqual(self.f5, Frac(0, 1))

    def test_neg(self):
        self.assertEqual(-self.f1, Frac(-6, 12))
        self.assertEqual(-self.f1, Frac(-3, 6))

        self.assertEqual(-self.f2, Frac(-5, 17))
        self.assertEqual(-self.f2, Frac(-10, 34))

        self.assertEqual(-self.f3, Frac(-2, 1))
        self.assertEqual(-self.f3, Frac(-6, 3))

        self.assertEqual(-self.f4, Frac(-1, 1))
        self.assertEqual(-self.f4, Frac(-5, 5))

        self.assertEqual(-self.f5, Frac(0, 3))
        self.assertEqual(-self.f5, Frac(0, 1))
        self.assertEqual(-self.f5, Frac(-0, 1))

    def test_invert(self):
        self.assertEqual(~self.f1, Frac(6, 3))
        self.assertEqual(~self.f1, Frac(2, 1))

        self.assertEqual(~self.f2, Frac(17, 5))
        self.assertEqual(~self.f2, Frac(34, 10))

        self.assertEqual(~self.f3, Frac(1, 2))
        self.assertEqual(~self.f3, Frac(3, 6))

        self.assertEqual(~self.f4, Frac(4, 4))
        self.assertEqual(~self.f4, Frac(1, 1))

        self.assertEqual(~self.f5, Frac(3, 0))

    def test_float(self):
        self.assertEqual(float(self.f1), 0.5)

        self.assertEqual(float(self.f2), 0.29411764705882354)

        self.assertEqual(float(self.f3), 2.0)

        self.assertEqual(float(self.f4), 1.0)

        self.assertEqual(float(self.f5), 0.0)

    def test_hash(self):
        self.assertEqual(self.f1.__hash__(), hash(3 / 6))
        self.assertEqual(self.f1.__hash__(), hash(1 / 2))

        self.assertEqual(self.f2.__hash__(), hash(5 / 17))
        self.assertEqual(self.f2.__hash__(), hash(10 / 34))

        self.assertEqual(self.f3.__hash__(), hash(2 / 1))
        self.assertEqual(self.f3.__hash__(), hash(6 / 3))

        self.assertEqual(self.f4.__hash__(), hash(4 / 4))
        self.assertEqual(self.f4.__hash__(), hash(3 / 3))

        self.assertEqual(self.f5.__hash__(), hash(0 / 3))
        self.assertEqual(self.f5.__hash__(), hash(0 / 2))


if __name__ == '__main__':
    unittest.main()
