from random import randint

from geometry import Rectangle
from points import Point


class Game:
    """
    Wraps geometry.Rectangle and points.Point into a guessing game.
    """

    @staticmethod
    def guess_rectangle_area(input_area: [int, float], rectangle_area: [str]) -> bool:
        """
        Returns a bool by evaluating equality between two floats, integers, or a mixture.
        """
        input_area_float = float(input_area)
        guess_result = rectangle_area == input_area_float
        if guess_result:
            print("You are right!")
            return True
        print(f"Wrong guess, rectangles area is {rectangle_area}!")
        print(f"Your area was off by {rectangle_area - input_area_float}")
        return False

    @staticmethod
    def create_random_rectangle():
        """
        Creates a random rectangle and prints a message.
        """
        random_rectangle = Rectangle(Point(randint(0, 9), randint(0, 9)), Point(randint(10, 19), randint(10, 19)))
        print("Random rectangle created!")
        return random_rectangle

    def game_guess_point(self):
        """
        Executes Game 1 - User guesses a point inside a random rectangle.
        """
        random_rectangle = self.create_random_rectangle()

        # Input user point coordinates.
        print("Input point coordinates. Try to fit your point inside the rectangle.")
        user_point = Point(float(input("Guess X: ")), float(input("Guess Y: ")))

        # Check if the user's point falls inside the rectangle.
        user_point.falls_in_rectangle(random_rectangle)

        # Print rectangle coordinates.
        random_rectangle.print_rectangle_coordinates()

    def game_guess_rectangle_area(self):
        """
        Executes Game 2 - User guesses the area of a random rectangle.
        """
        random_rectangle_2 = self.create_random_rectangle()

        # Input user guess for rectangle area.
        user_rectangle_area = input("Guess rectangle area: ")

        # Check if the user's guess is correct.
        self.guess_rectangle_area(user_rectangle_area, random_rectangle_2.calculate_rectangle_area())
