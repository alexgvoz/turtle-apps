from turtle import Turtle


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10


class Player(Turtle):

    def __init__(self, screen):
        super().__init__()
        self.penup()
        self.setheading(90)
        self.shape("turtle")
        self.color("gray66")
        self.goToStart()

        screen.listen()
        screen.onkeypress(self.move, "Up")

    def move(self):
        self.forward(MOVE_DISTANCE)

    def goToStart(self):
        self.goto(STARTING_POSITION)
