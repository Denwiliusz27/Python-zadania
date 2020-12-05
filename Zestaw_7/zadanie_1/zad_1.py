from points import Point


class Rectangle:
    """Klasa reprezentująca prostokąty na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
        # Chcemy, aby x1 < x2, y1 < y2.
        if x1 < x2 and y1 < y2:
            self.pt1 = Point(x1, y1)
            self.pt2 = Point(x2, y2)
        else:
            raise ValueError

    def __str__(self): # "[(x1, y1), (x2, y2)]"
        return "[{0}, {1}]" .format(self.pt1, self.pt2)

    def __repr__(self):  # "Rectangle(x1, y1, x2, y2)"
        return "Rectanngle({0}, {1}, {2}, {3})".format(self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y)

    def __eq__(self, other): # obsługa rect1 == rect2
        return self.pt1 == other.pt1 and self.pt2 == other.pt2

    def __ne__(self, other):  # obsługa rect1 != rect2
        return not self == other

    def center(self): # zwraca środek prostokąta
        x = (self.pt2.x + self.pt1.x) / 2
        y = (self.pt2.y + self.pt1.y) / 2
        return Point(x, y)

    def area(self):  # pole powierzchni
        x = self.pt2.x - self.pt1.x
        y = self.pt2.y - self.pt1.y
        return x*y

    def move(self, x, y):  # przesunięcie o (x, y)
        self.pt1 += Point(x, y)
        self.pt2 += Point(x, y)
        return self


    def intersection(self, other):  # część wspólna prostokątów
        x = min(self.pt2.x, other.pt2.x) - max(self.pt1.x, other.pt1.x)
        y = min(self.pt2.y, other.pt2.y) - max(self.pt1.y, other.pt1.y)
        if x >= 0 and y >=0:
            return x*y
        else:
            return 0

        """if self.pt1.x <= other.pt1.x <= self.pt2.x:
            print("warunek1")
            if self.pt1.y <= other.pt1.y <= self.pt2.y:
                print("warunek2")
                if self.pt1.x <= other.pt2.x <= self.pt2.x:
                    print("warunek3")
                    if self.pt1.y <= other.pt2.y <= self.pt2.y:
                        print("warunek4")
                        return other.area()  # jeden wewnatrz drugiego
                    else:  # jeden wychodzi z gory drugiego
                        print("warunek5")
                        p1 = other.pt1
                        p2 = Point(other.pt2.x, self.pt2.y)
                        return Rectangle(p1.x, p1.y, p2.x, p2.y).area()
        """

    def cover(self, other):
        pass  # prostąkąt nakrywający oba

    def make4(self):
        pass  # zwraca krotkę czterech mniejszych


# Kod testujący moduł.

import unittest

# class TestRectangle(unittest.TestCase): pass

if __name__ == '__main__':
    try:
        rec1 = Rectangle(1, 1, 4, 5)
    except ValueError:
        print("valuerror 1")
    finally:
        print("zrobilem")

    try:
        rec2 = Rectangle(1, 1, 3, 4)
    except ValueError:
        print("valuerror 2")
    finally:
        print("zrobilem")


    print(rec1)
    print(rec2)
    print(rec1.__repr__())
    print(rec2.__repr__())
    print(rec1 == rec2)
    print(rec1 != rec2)
    print(rec1.center())
    print(rec1.area())
    print("#####cz_wspolna######")
    rec3 = Rectangle(4, 1, 6, 5)
    print(rec1.intersection(rec3))
    print("#####cz_wspolna######")

    print(rec1.move(3, -2))

"""  try:
        rec2 = Rectangle(3, 3, 1, 1)
    except ValueError:
        print("valuerror 2")

    try:
        rec3 = Rectangle(1, 2, 8, 6)
        print("zrobilem 2")
    except ValueError:
        print("valuerror 3")
"""