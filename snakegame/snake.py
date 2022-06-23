import time
from turtle import Turtle

MOVE_DIST = 10


class Snake:
    segments = []

    def __init__(self, screen):
        self.screen = screen
        self.screen.listen()
        self.screen.onkeypress(self.up, "Up")
        self.screen.onkeypress(self.down, "Down")
        self.screen.onkeypress(self.left, "Left")
        self.screen.onkeypress(self.right, "Right")

        self.createSnake()
        self.head = self.segments[0]
        self.moveSnake()

    def createSnake(self):
        for i in range(3):
            self.segments.append(Turtle("square"))
            self.segments[i].penup()
            self.segments[i].color("light gray")
            self.segments[i].setx(0 - (20 * i))

    def moveSnake(self):
        while True:
            self.screen.update()
            time.sleep(.05)

            for s in range(len(self.segments) - 1, -1, -1):
                if s == 0:
                    self.head.forward(MOVE_DIST)
                else:
                    self.segments[s].setposition(self.segments[s - 1].position())

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
