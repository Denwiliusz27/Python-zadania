from points import Point
from math import pi, sqrt
import unittest


class Circle:
    """Klasa reprezentująca okręgi na płaszczyźnie."""

    def __init__(self, x, y, radius):
        if radius < 0:
            raise ValueError("promień ujemny")
        self.pt = Point(x, y)
        self.radius = radius

    def __repr__(self):  # "Circle(x, y, radius)"
        return "Circle({0}, {1}, {2})".format(self.pt.x, self.pt.y, self.radius)

    def __eq__(self, other):
        return self.pt == other.pt and self.radius == other.radius

    def __ne__(self, other):
        return not self == other

    def area(self):  # pole powierzchni
        return pi * (self.radius ** 2)

    def move(self, x, y):  # przesuniecie o (x, y)
        self.pt += Point(x, y)
        return self

    def cover(self, other):  # najmniejszy okrąg pokrywający oba
        odl = sqrt((other.pt.x - self.pt.x) ** 2 + (other.pt.y - self.pt.y) ** 2)
        r_min = min(self.radius, other.radius)
        r_max = max(self.radius, other.radius)

        if r_min + odl <= r_max:
            if self.radius > other.radius:
                return Circle(self.pt.x, self.pt.y, self.radius)
            else:
                return Circle(other.pt.x, other.pt.y, other.radius)
        else:
            r = (self.radius + other.radius + odl) / 2
            x = self.pt.x + (r - self.radius) * (other.pt.x - self.pt.x) / odl
            y = self.pt.y + (r - self.radius) * (other.pt.y - self.pt.y) / odl
            return Circle(x, y, r)


# Kod testujący moduł.

class TestCircle(unittest.TestCase):
    def test_correct_input(self):
        try:
            circle = Circle(1, 3, 4)
        except ValueError:
            self.fail()

    def test_wrong_input(self):
        self.assertRaises(ValueError, Circle, 0, 3, -3)

    def setUp(self):
        self.c = Circle(1, 3, 4)
        self.c1 = Circle(1, 3, 2)

        self.c1_r = Circle(2, 3, 1.5)  # od prawej
        self.c2_r = Circle(2, 3, 3)
        self.c3_r = Circle(4, 3, 2)
        self.c4_r = Circle(5, 3, 3)
        self.c5_r = Circle(7, 3, 2)
        self.c6_r = Circle(7, 3, 4)
        self.c7_r = Circle(8, 3, 2)

        self.c1_g = Circle(1, 4, 1.5)  # od gory
        self.c2_g = Circle(1, 4, 3)
        self.c3_g = Circle(1, 6, 2)
        self.c4_g = Circle(1, 7, 3)
        self.c5_g = Circle(1, 9, 2)
        self.c6_g = Circle(1, 9, 4)
        self.c7_g = Circle(1, 10, 2)

    def test_init(self):
        self.assertEqual(self.c.pt, Point(1, 3))
        self.assertEqual(self.c.radius, 4)

    def test_repr(self):
        self.assertEqual(self.c.__repr__(), "Circle(1, 3, 4)")

    def test_cmp(self):
        self.assertTrue(self.c == Circle(1, 3, 4))
        self.assertFalse(self.c == Circle(3, 1, 4))

        self.assertTrue(self.c != Circle(3, 1, 4))
        self.assertFalse(self.c != Circle(1, 3, 4))

    def test_area(self):
        self.assertEqual(self.c.area(), 16 * pi)
        self.assertEqual(Circle(2, -2, 3).area(), 9 * pi)
        self.assertEqual(Circle(-1, 2, 3).area(), 9 * pi)
        self.assertEqual(Circle(-3, -2, 3).area(), 9 * pi)
        self.assertEqual(Circle(0, 0, 3).area(), 9 * pi)
        self.assertEqual(Circle(3, 4, 0).area(), 0)

    def test_move(self):
        self.assertEqual(Circle(1, 3, 4).move(2, 0), Circle(3, 3, 4))
        self.assertEqual(Circle(1, 3, 4).move(2, 1), Circle(3, 4, 4))
        self.assertEqual(Circle(1, 3, 4).move(0, 3), Circle(1, 6, 4))
        self.assertEqual(Circle(1, 3, 4).move(2, -2), Circle(3, 1, 4))
        self.assertEqual(Circle(1, 3, 4).move(0, -1), Circle(1, 2, 4))
        self.assertEqual(Circle(1, 3, 4).move(-1, 0), Circle(0, 3, 4))
        self.assertEqual(Circle(1, 3, 4).move(-1, 2), Circle(0, 5, 4))
        self.assertEqual(Circle(1, 3, 4).move(-2, 0), Circle(-1, 3, 4))
        self.assertEqual(Circle(1, 3, 4).move(-2, -1), Circle(-1, 2, 4))

    def test_cover(self):
        self.assertEqual(self.c.cover(self.c1), Circle(1, 3, 4))




if __name__ == '__main__':
    unittest.main()

"""    c = Circle(0, 0, 3)
    c1 = Circle(4, 0, 2)

    print(c.__repr__())
    print(c.area())
    print(c.cover(c1))
    print(c1.cover(c))
    print(c.cover(Circle(1,0,2)))
"""
