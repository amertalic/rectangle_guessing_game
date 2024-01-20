# Rectangle Guessing Game

**Rectangle Guessing Game** is a simple Python console game where you have to guess properties of randomly generated rectangle.

## Installation

1. Clone the repository
2. Navigate to the project directory:`cd rectangle-guessing-game`
3. Run the game: `python main.py`
## How to Play
The game consists of two rounds:

### Game 1: Guessing a Point Inside a Rectangle
A random rectangle will be generated with coordinates.

You need to input a point's coordinates and guess if it falls inside the rectangle.

The program will tell you if your guess is correct and display the rectangle's coordinates.

### Game 2: Guessing the Area of a Rectangle
Another random rectangle will be generated.

You need to input your guess for the rectangle's area.

The program will inform you if your guess is correct and reveal the actual area.

## File Structure
- main.py: The main script to run the game.
- game.py: Contains the Game class with methods for playing the game.
- geometry.py: Defines the Rectangle class for working with rectangles.
- points.py: Defines the Point class for working with points.
