import time
from turtle import Turtle

from ponggame.paddles import Paddle
from ponggame.pongball import Ball
from ponggame.scoreboard import Scoreboard


class PongGame:

    def start(self, screen):
        screen.setup(800, 600)
        screen.title("Pong")
        screen.tracer(0)

        self.drawMiddle()

        game_is_on = True

        r_paddle = Paddle(350, "tomato4")
        l_paddle = Paddle(-350,"RoyalBlue4")
        ball = Ball()
        scoreboard = Scoreboard()

        screen.listen()
        screen.onkeypress(r_paddle.up, "Up")
        screen.onkeypress(r_paddle.down, "Down")
        screen.onkeypress(l_paddle.up, "w")
        screen.onkeypress(l_paddle.down, "s")

        while game_is_on:
            screen.update()
            time.sleep(0.01)
            ball.move()

            if ball.distance(r_paddle) < 50 and ball.xcor() > 340:
                ball.bounceX()

            if ball.distance(l_paddle) < 50 and ball.xcor() < -340:
                ball.bounceX()

            if ball.xcor() > 400:
                ball.reset()
                scoreboard.rightPoint()

            if ball.xcor() < -400:
                ball.reset()
                scoreboard.leftPoint()

            if ball.ycor() < -280 or ball.ycor() > 280:
                ball.bounceY()

        screen.exitonclick()

    def drawMiddle(self):
        tim = Turtle()
        tim.hideturtle()
        tim.penup()
        tim.speed(0)
        tim.goto(0, 300)
        tim.pencolor("gray66")
        tim.pensize(3)
        tim.right(90)

        for i in range(31):
            if i % 2 == 0:
                tim.pendown()
            else:
                tim.penup()

            tim.forward(20)