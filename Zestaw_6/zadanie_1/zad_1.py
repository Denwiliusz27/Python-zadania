import unittest


class Point:
    """Klasa reprezentująca punkty na płaszczyźnie."""

    def __init__(self, x, y):  # konstuktor
        self.x = x
        self.y = y

    def __str__(self):  # zwraca string "(x, y)"
        return "({}, {})".format(self.x, self.y)

    def __repr__(self):  # zwraca string "Point(x, y)"
        return "Point({}, {})".format(self.x, self.y)

    def __eq__(self, other):  # obsługa point1 == point2
        return (self.x == other.x) and (self.y == other.y)

    def __ne__(self, other):  # obsługa point1 != point2
        return not ((self.x == other.x) and (self.y == other.y))

    # Punkty jako wektory 2D.
    def __add__(self, other):  # v1 + v2
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):  # v1 - v2
        return Point(self.x - other.x, self.y - other.y)

    # self.x -= other.x
    # self.y -= other.y

    def __mul__(self, other):  # v1 * v2, iloczyn skalarny (liczba)
        return self.x * other.x + self.y * other.y

    def cross(self, other):  # v1 x v2, iloczyn wektorowy 2D (liczba)
        return self.x * other.y - self.y * other.x

    def length(self):  # długość wektora
        return self.x ** 2 + self.y ** 2

    def __hash__(self):
        return hash((self.x, self.y))  # bazujemy na tuple, immutable points


# Kod testujący moduł.

class TestPoint(unittest.TestCase):
    def setUp(self): pass

    def test_print(self):
        self.assertEqual(Point(2, 3).__str__(), "(2, 3)")
        self.assertNotEqual(Point(2, 3).__str__(), "(3, 2)")
        self.assertEqual(Point(2, 3).__repr__(), "Point(2, 3)")
        self.assertNotEqual(Point(2, 3).__repr__(), "Point(3, 2)")

    def test_cmp(self):
        self.assertTrue(Point(2, 3) == Point(2, 3))
        self.assertFalse(Point(2, 3) == Point(3, 2))
        self.assertTrue(Point(2, 3) != Point(3, 2))
        self.assertFalse(Point(2, 3) != Point(2, 3))

    def test_add(self):
        self.assertEqual(Point(2, 3) + Point(3, 2), Point(5, 5))
        self.assertNotEqual(Point(2, 3) + Point(3, 2), Point(-1, 1))

    def test_sub(self):
        self.assertEqual(Point(2, 3) - Point(3, 2), Point(-1, 1))
        self.assertNotEqual(Point(2, 3) - Point(3, 2), Point(5, 5))

    def test_mul(self):
        self.assertEqual(Point(2, 3) * Point(3, 2), 12)
        self.assertNotEqual(Point(2, 3) * Point(3, 2), 5)

    def test_cross(self):
        self.assertEqual(Point(2, 3).cross(Point(3, 2)), -5)
        self.assertNotEqual(Point(2, 3).cross(Point(3, 2)), 0)

    def test_length(self):
        self.assertEqual(Point(2, 3).length(), 13)
        self.assertNotEqual(Point(2, 3).length(), 5)

    def test_hash(self):
        p = Point(2, 3)
        self.assertEqual(p.__hash__(), hash(p))


if __name__ == '__main__':
    unittest.main()
"""
    p1 = Point(1, 2)
    p2 = Point(3, 4)
    print(p1.cross(p2))

    p1 = Point(4, 5)
    p2 = Point(3, 2)
    print(p1 != p2)
    print(p1 == p2)
    print(p1 + p2)
    print(p1 - p2)
    print("#################")
    print("rep:", p1.__repr__())
    print("str:", p1.__str__())
    print("p1==p2: ", p1.__eq__(p2))
    print("p1 != p2: ", p1.__ne__(p2))
    print("p1 + p2: ", p1.__add__(p2))
    print("p1 - p2: ", p1.__sub__(p2))
    print("p1 * p2: ", p1.__mul__(p2))
    print("p1 x p2: ", p1.cross(p2))
    print("|p1|: ", p1.length())
    print("#################")

    print(p1.length())
    print(p1)
"""
