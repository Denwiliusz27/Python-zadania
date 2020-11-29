class Point:
    """Klasa reprezentująca punkty na płaszczyźnie."""

    def __init__(self, x, y):  # konstuktor
        self.x = x
        self.y = y

    def __str__(self):  # zwraca string "(x, y)"
        return "({0}, {1})".format(self.x, self.y)

    def __repr__(self):  # zwraca string "Point(x, y)"
        return "Point({0}, {1})".format(self.x, self.y)

    def __eq__(self, other):   # obsługa point1 == point2
        return (self.x == other.x) and (self.y == other.y)

    def __ne__(self, other):  # obsługa point1 != point2
        return not ((self.x == other.x) and (self.y == other.y))

    # Punkty jako wektory 2D.
    def __add__(self, other):  # v1 + v2
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):   # v1 - v2
        return Point(self.x - other.x, self.y - other.y)
       # self.x -= other.x
       # self.y -= other.y

    def __mul__(self, other):   # v1 * v2, iloczyn skalarny (liczba)
        return self.x * other.x + self.y * other.y

    def cross(self, other):  # v1 x v2, iloczyn wektorowy 2D (liczba)
        return self.x * other.y - self.y * other.x

    def length(self):   # długość wektora
        return self.x**2 + self.y**2

    def __hash__(self):
        return hash((self.x, self.y))  # bazujemy na tuple, immutable points


# Kod testujący moduł.

# import unittest

# class TestPoint(unittest.TestCase): pass

if __name__ == '__main__':
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
    print("|p1|", p1.length())
    print("#################")

    print(p1.length())
    print(p1)
