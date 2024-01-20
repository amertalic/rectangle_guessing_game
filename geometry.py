class Rectangle:
    """
    A rectangle object in a coordinate system can be defined by two points: upright and lower left.

    Example:

         y
         |
    13   +------------------- (12,13) upper right
         |                   |
         |                   |
         |    +-----------+  |
         |    |           |  |
         |    |           |  |
         |    +-----------+  |
    5    +-------------------+----
         (6,5) lower left        x
"""

    def __init__(self, lowleft: [int, float], upright: [int, float]):
        self.point1 = lowleft
        self.point2 = upright

    def print_rectangle_coordinates(self):
        print(
            f"Rectangle Coordinates: {self.point1.x}, {self.point1.y} and  {self.point2.x}, {self.point2.y}"

        )

    def calculate_rectangle_area(self) -> [float, int]:
        """
        Calculate distance between x and y.
        """
        rectangle_area = (self.point2.x - self.point1.x) * (self.point2.y - self.point1.y)
        print(f"Rectangle are is: {rectangle_area}")
        return rectangle_area
