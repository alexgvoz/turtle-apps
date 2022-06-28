from turtle import Turtle

MOVE_DIST = 10
COLOR = "gray66"

class Snake:
    segments = []

    def __init__(self, screen):
        screen.listen()
        screen.onkeypress(self.up, "Up")
        screen.onkeypress(self.down, "Down")
        screen.onkeypress(self.left, "Left")
        screen.onkeypress(self.right, "Right")

        for i in range(3):
            self.segments.append(Turtle("square"))
            self.segments[i].penup()
            self.segments[i].color(COLOR)
            self.segments[i].setx(0 - (20 * i))

        self.head = self.segments[0]
        self.move()

    def move(self):
        for s in range(len(self.segments) - 1, -1, -1):
            if s == 0:
                self.head.forward(MOVE_DIST)
            else:
                self.segments[s].setposition(self.segments[s - 1].position())

    def extend(self):
        self.segments.append(Turtle("square"))
        self.segments[-1].penup()
        self.segments[-1].color(COLOR)
        self.segments[-1].setposition(self.segments[-2].position())

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
