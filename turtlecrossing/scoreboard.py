from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("gray66")
        self.goto(-205, 255)
        self.level = 0
        self.write(f"Level: {self.level}", False, "center", FONT)

    def update(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}", False, "center", FONT)

    def gameOver(self):
        self.goto(0,0)
        self.write("Game Over", False, "center", FONT)
