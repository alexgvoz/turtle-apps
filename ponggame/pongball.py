from turtle import Turtle
from random import choice

BALL_SPEED = 4


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("gray66")
        self.setheading(45)
        self.move_speed = 0.1
        self.y_move = choice([-BALL_SPEED, BALL_SPEED])
        self.x_move = choice([-BALL_SPEED, BALL_SPEED])

    def move(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def bounceY(self):
        self.y_move = -self.y_move
        self.move_speed *= 0.9

    def bounceX(self):
        self.x_move = -self.x_move
        self.move_speed *= 0.9

    def reset(self):
        self.home()
        self.bounceX()
        self.move_speed = 0.1
