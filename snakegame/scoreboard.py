from turtle import Turtle

FONT = ("Arial", 16, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.sety(270)
        self.score = 0
        self.hideturtle()
        self.pencolor("gray66")
        self.write(f"Score: {self.score}", False, "center", FONT)

    def updateScore(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", False, "center", FONT)

    def gameOver(self):
        self.home()
        self.write("GAME OVER", False, "center", FONT)
