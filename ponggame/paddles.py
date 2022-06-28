from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, startX):
        super().__init__()
        self.shape("square")
        self.penup()
        self.setheading(90)
        self.color("gray66")
        self.shapesize(1, 5)
        self.goto(startX, 0)

    def up(self):
        if self.ycor() < 250:
            self.forward(10)

    def down(self):
        if self.ycor() > -250:
            self.backward(10)
