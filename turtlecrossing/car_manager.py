from turtle import Turtle
from random import choice, randrange

COLORS = ["tomato4", "darkorange", "DarkGoldenrod3", "OliveDrab4", "RoyalBlue4", "maroon4"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    carspeed = STARTING_MOVE_DISTANCE

    def spawnTurtle(self):
        car = Turtle()
        car.penup()
        car.setposition(300, randrange(-240, 250, 10))
        car.color(choice(COLORS))
        car.setheading(180)
        car.forward(10)

