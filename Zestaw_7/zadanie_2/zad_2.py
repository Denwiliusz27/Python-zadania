from math import pi, sqrt
import unittest
from points import Point


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
            rec = Circle(1, )
        except ValueError:
            self.fail()


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
