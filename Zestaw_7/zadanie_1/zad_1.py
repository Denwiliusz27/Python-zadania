from points import Point
import unittest


class Rectangle:
    """Klasa reprezentująca prostokąty na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
        # Chcemy, aby x1 < x2, y1 < y2.
        if x1 < x2 and y1 < y2:
            self.pt1 = Point(x1, y1)
            self.pt2 = Point(x2, y2)
        else:
            raise ValueError

    def __str__(self):  # "[(x1, y1), (x2, y2)]"
        return "[{0}, {1}]".format(self.pt1, self.pt2)

    def __repr__(self):  # "Rectangle(x1, y1, x2, y2)"
        return "Rectangle({0}, {1}, {2}, {3})".format(self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y)

    def __eq__(self, other):  # obsługa rect1 == rect2
        return self.pt1 == other.pt1 and self.pt2 == other.pt2

    def __ne__(self, other):  # obsługa rect1 != rect2
        return not self == other

    def center(self):  # zwraca środek prostokąta
        x = (self.pt2.x + self.pt1.x) / 2
        y = (self.pt2.y + self.pt1.y) / 2
        return Point(x, y)

    def area(self):  # pole powierzchni
        x = self.pt2.x - self.pt1.x
        y = self.pt2.y - self.pt1.y
        return x * y

    def move(self, x, y):  # przesunięcie o (x, y)
        self.pt1 += Point(x, y)
        self.pt2 += Point(x, y)
        return self

    def intersection(self, other):  # część wspólna prostokątów
        x = min(self.pt2.x, other.pt2.x) - max(self.pt1.x, other.pt1.x)
        y = min(self.pt2.y, other.pt2.y) - max(self.pt1.y, other.pt1.y)

        if x >= 0 and y >= 0:
            return x * y
        else:
            return 0

    def cover(self, other):  # prostąkąt nakrywający oba
        x1 = min(self.pt1.x, other.pt1.x)
        y1 = min(self.pt1.y, other.pt1.y)
        x2 = max(self.pt2.x, other.pt2.x)
        y2 = max(self.pt2.y, other.pt2.y)
        return Rectangle(x1, y1, x2, y2)

    def make4(self):  # zwraca krotkę czterech mniejszych
        center = self.center()

        r1 = Rectangle(self.pt1.x, self.pt1.y, center.x, center.y)
        r2 = Rectangle(center.x, center.y, self.pt2.x, self.pt2.y)
        r3 = Rectangle(self.pt1.x, center.y, center.x, self.pt2.y)
        r4 = Rectangle(center.x, self.pt1.y, self.pt2.x, center.y)

        return r1, r2, r3, r4


# Kod testujący moduł.

class TestRectangle(unittest.TestCase):
    def test_correct_input(self):
        try:
            rec = Rectangle(4, 2, 6, 5)
        except ValueError:
            self.fail()

    def test_wrong_input(self):
        self.assertRaises(ValueError, Rectangle, 2, 1, 1, 5)
        self.assertRaises(ValueError, Rectangle, 2, 4, 3, 2)

    def setUp(self):
        self.r = Rectangle(1, 1, 6, 5)
        self.r1 = Rectangle(2, 3, 4, 6)  # gora
        self.r2 = Rectangle(4, 2, 7, 6)  # prawy gorny
        self.r3 = Rectangle(4, 1, 7, 3)  # prawo
        self.r4 = Rectangle(5, -1, 7, 2)  # prawy dolny
        self.r5 = Rectangle(2, -1, 4, 4)  # dol
        self.r6 = Rectangle(0, -1, 2, 2)  # lewy dolny
        self.r7 = Rectangle(-1, 2, 2, 5)  # lewy
        self.r8 = Rectangle(2, 2, 4, 5)  # wewnarz
        self.r9 = Rectangle(0, 0, 7, 8)  # zewnatrz
        self.r10 = Rectangle(0, 2, 7, 5)  # przez boki
        self.r11 = Rectangle(2, -1, 4, 7)  # przez podstawy

    def test_init(self):
        self.assertEqual(self.r.pt1, Point(1, 1))
        self.assertEqual(self.r.pt2, Point(6, 5))

    def test_print(self):
        self.assertEqual(self.r.__str__(), "[(1, 1), (6, 5)]")
        self.assertEqual(self.r.__repr__(), "Rectangle(1, 1, 6, 5)")

    def test_cmp(self):
        self.assertTrue(self.r == Rectangle(1, 1, 6, 5))
        self.assertFalse(self.r == Rectangle(1, 1, 5, 6))

        self.assertTrue(self.r != Rectangle(2, 2, 4, 5))
        self.assertFalse(self.r2 != Rectangle(4, 2, 7, 6))

    def test_center(self):
        self.assertEqual(self.r.center(), Point(3.5, 3))
        self.assertEqual(self.r1.center(), Point(3, 4.5))

    def test_area(self):
        self.assertEqual(self.r.area(), 20)
        self.assertEqual(self.r1.area(), 6)

    def test_intersection(self):
        self.assertEqual(self.r.intersection(self.r1), 4)
        self.assertEqual(self.r.intersection(self.r2), 6)
        self.assertEqual(self.r.intersection(self.r3), 4)
        self.assertEqual(self.r.intersection(self.r4), 1)
        self.assertEqual(self.r.intersection(self.r5), 6)
        self.assertEqual(self.r.intersection(self.r6), 1)
        self.assertEqual(self.r.intersection(self.r7), 3)
        self.assertEqual(self.r.intersection(self.r8), 6)
        self.assertEqual(self.r.intersection(self.r9), 20)
        self.assertEqual(self.r.intersection(self.r10), 15)
        self.assertEqual(self.r.intersection(self.r11), 8)

    def test_cover(self):
        self.assertEqual(self.r.cover(self.r1), Rectangle(1, 1, 6, 6))
        self.assertEqual(self.r.cover(self.r2), Rectangle(1, 1, 7, 6))
        self.assertEqual(self.r.cover(self.r3), Rectangle(1, 1, 7, 5))
        self.assertEqual(self.r.cover(self.r4), Rectangle(1, -1, 7, 5))
        self.assertEqual(self.r.cover(self.r5), Rectangle(1, -1, 6, 5))
        self.assertEqual(self.r.cover(self.r6), Rectangle(0, -1, 6, 5))
        self.assertEqual(self.r.cover(self.r7), Rectangle(-1, 1, 6, 5))
        self.assertEqual(self.r.cover(self.r8), Rectangle(1, 1, 6, 5))
        self.assertEqual(self.r.cover(self.r9), Rectangle(0, 0, 7, 8))
        self.assertEqual(self.r.cover(self.r10), Rectangle(0, 1, 7, 5))
        self.assertEqual(self.r.cover(self.r11), Rectangle(1, -1, 6, 7))

    def test_make4(self):
        self.assertEqual(self.r.make4(), (Rectangle(1, 1, 3.5, 3), Rectangle(3.5, 3, 6, 5),
                                          Rectangle(1, 3, 3.5, 5), Rectangle(3.5, 1, 6, 3)))

    def test_move(self):
        self.assertEqual(self.r.move(3, -2), Rectangle(4, -1, 9, 3))


if __name__ == '__main__':
    unittest.main()