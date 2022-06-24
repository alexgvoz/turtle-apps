from turtle import Turtle
from random import randrange


class Food(Turtle):

    def __init__(self):
        super().__init__()
        print("Food is a go!")
        self.shape("circle")
        self.penup()
        self.shapesize(0.5,0.5)
        self.color("tomato4")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.goto(randrange(-290, 290), randrange(-290, 290))

