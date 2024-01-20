from math import sqrt

from geometry import Rectangle


class Point:

    def __init__(self, x: [int, float], y: [int, float]):
        self.x = x
        self.y = y

    def falls_in_rectangle(self, rectangle: 'Rectangle') -> bool:
        """
        Checks if coordinates are in rectangle.
        """
        in_rectangle = rectangle.point1.x < self.x < rectangle.point2.x and rectangle.point1.y < self.y < rectangle.point2.y
        print(f"Your point was inside rectangle: {in_rectangle}")
        return in_rectangle

    def calculate_distance_from_point(self, point: 'Point') -> [int, float]:
        """
        Calculate distance between x and y.
        """
        return sqrt((self.x - point.x) ** 2 + (self.y - point.y) ** 2)
