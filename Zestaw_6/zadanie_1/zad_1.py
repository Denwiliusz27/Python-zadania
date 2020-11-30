import unittest, math


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
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):  # obsługa point1 != point2
        return not (self.x == other.x and self.y == other.y)

    # Punkty jako wektory 2D.
    def __add__(self, other):  # v1 + v2
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):  # v1 - v2
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):  # v1 * v2, iloczyn skalarny (liczba)
        return self.x * other.x + self.y * other.y

    def cross(self, other):  # v1 x v2, iloczyn wektorowy 2D (liczba)
        return self.x * other.y - self.y * other.x

    def length(self):  # długość wektora
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __hash__(self):
        return hash((self.x, self.y))  # bazujemy na tuple, immutable points


# Kod testujący moduł.

class TestPoint(unittest.TestCase):
    def setUp(self):
        self.p1 = Point(2, 3)
        self.p2 = Point(4, 1)

    def test_init(self):
        self.assertEqual(self.p1.x, 2.000000)
        self.assertEqual(self.p1.x, 2)
        self.assertNotEqual(self.p1.x, 3)
        self.assertEqual(self.p1.y, 3)
        self.assertEqual(self.p1.y, 3.000000)
        self.assertNotEqual(self.p1.y, 2)

        self.assertEqual(self.p2.x, 4)
        self.assertEqual(self.p2.x, 4.0000)
        self.assertNotEqual(self.p2.x, 1)
        self.assertEqual(self.p2.y, 1)
        self.assertEqual(self.p2.y, 1.0000)
        self.assertNotEqual(self.p1.y, 4)

    def test_print(self):
        self.assertEqual(self.p1.__str__(), "(2, 3)")
        self.assertNotEqual(self.p1.__str__(), "(3, 2)")
        self.assertEqual(self.p1.__repr__(), "Point(2, 3)")
        self.assertNotEqual(self.p1.__repr__(), "Point(3, 2)")

        self.assertEqual(self.p2.__str__(), "(4, 1)")
        self.assertNotEqual(self.p2.__str__(), "(1, 4)")
        self.assertEqual(self.p2.__repr__(), "Point(4, 1)")
        self.assertNotEqual(self.p2.__repr__(), "Point(1, 4)")

    def test_cmp(self):
        self.assertTrue(self.p1 == Point(2, 3))
        self.assertFalse(self.p1 == Point(3, 2))
        self.assertTrue(self.p1 != Point(3, 2))
        self.assertFalse(self.p1 != Point(2, 3))

        self.assertTrue(self.p2 == Point(4, 1))
        self.assertFalse(self.p2 == Point(1, 4))
        self.assertTrue(self.p2 != Point(1, 4))
        self.assertFalse(self.p2 != Point(4, 1))

    def test_add(self):
        self.assertEqual(self.p1 + self.p2, Point(6, 4))
        self.assertEqual(self.p2 + self.p1, Point(6, 4))
        self.assertNotEqual(self.p1 + self.p2, Point(4, 6))
        self.assertNotEqual(self.p2 + self.p1, Point(4, 6))

    def test_sub(self):
        self.assertEqual(self.p1 - self.p2, Point(-2, 2))
        self.assertEqual(self.p2 - self.p1, Point(2, -2))
        self.assertNotEqual(self.p1 - self.p2, Point(2, -2))
        self.assertNotEqual(self.p2 - self.p1, Point(-2, 2))

    def test_mul(self):
        self.assertEqual(self.p1 * self.p2, 11)
        self.assertEqual(self.p2 * self.p1, 11)
        self.assertNotEqual(self.p2 * self.p1, 14)
        self.assertNotEqual(self.p1 * self.p2, 14)

    def test_cross(self):
        self.assertEqual(self.p1.cross(self.p2), -10)
        self.assertNotEqual(self.p1.cross(self.p2), 10)

        self.assertEqual(self.p2.cross(self.p1), 10)
        self.assertNotEqual(self.p2.cross(self.p1), -10)

    def test_length(self):
        self.assertEqual(self.p1.length(), math.sqrt(13))
        self.assertNotEqual(self.p1.length(), 13)

        self.assertEqual(self.p2.length(), math.sqrt(17))
        self.assertNotEqual(self.p2.length(), 17)

    def test_hash(self):
        self.assertEqual(self.p1.__hash__(), hash((2, 3)))
        self.assertNotEqual(self.p1.__hash__(), hash(self.p2))

        self.assertEqual(self.p2.__hash__(), hash((4, 1)))
        self.assertNotEqual(self.p2.__hash__(), hash(self.p1))


if __name__ == '__main__':
    unittest.main()
