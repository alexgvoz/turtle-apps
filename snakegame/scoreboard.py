from turtle import Turtle

FONT = ("Arial", 16, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.pencolor("gray66")

        with open("snakegame/data.txt", mode="r") as data:
            self.highscore = int(data.read())

        self.update()

    def update(self):
        self.clear()
        self.goto(-250, 270)
        self.write(f"Score: {self.score}", False, "center", FONT)
        self.goto(210, 270)
        self.write(f"Highscore: {self.highscore}", False, "center", FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score

            with open("snakegame/data.txt", mode="w") as data:
                data.write(str(self.highscore))

        self.score = 0
        self.update()

    def increaseScore(self):
        self.score += 1
