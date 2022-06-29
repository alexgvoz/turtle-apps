import time
from turtle import Turtle
from random import choice, randrange

COLORS = ["tomato4", "darkorange", "DarkGoldenrod3", "OliveDrab4", "RoyalBlue4", "maroon4"]

class CarManager:

    def __init__(self):
        self.activecars = []
        self.carspeed = 5

    def spawnTurtle(self):
        if randrange(1,6) == 1:
            car = Turtle()
            car.penup()
            car.shape("square")
            car.shapesize(1, 2)
            car.setposition(300, randrange(-240, 250, 25))
            car.color(choice(COLORS))
            car.setheading(180)
            self.activecars.append(car)

    def moveCars(self):
        for car in self.activecars:
            car.forward(self.carspeed)

    def speedUp(self):
        self.carspeed += 1

    def nearPlayer(self, player):
        for car in self.activecars:
            print(self.activecars.index(car))
            print(car.distance(player))
            if car.distance(player) < 20:
                return True
            else:
                return False

    def cleanUp(self):
        for car in self.activecars:
            if car.xcor() < -320:
                self.activecars.remove(car)
