from turtle import Turtle, Screen
from random import choice

tim = Turtle()
screen = Screen()

screen.colormode(255)
screen.title("Hirst Painting Simulator")
screen.setup(1000, 1000)
screen.bgcolor("#333333")
tim.shapesize(2)
tim.pensize(5)
tim.fillcolor("dark slate gray")

colors = ["dark slate gray", "dark slate blue", "cadet blue", "sea green", "dark khaki", "tomato4", "SlateBlue2",
          "RoyalBlue4"]


def moveForwards():
    tim.pencolor(choice(colors))
    tim.forward(30)


def moveBack():
    tim.pencolor(choice(colors))
    tim.back(30)


def tiltLeft():
    heading = tim.heading() + 10
    tim.setheading(heading)


def tiltRight():
    heading = tim.heading() - 10
    tim.setheading(heading)


def clearScreen():
    tim.clear()
    tim.hideturtle()
    tim.speed(0)
    tim.penup()
    tim.home()
    tim.pendown()
    tim.showturtle()


screen.listen()
screen.onkey(fun=moveForwards, key="w")
screen.onkey(fun=moveBack, key="s")
screen.onkeypress(fun=tiltLeft, key="a")
screen.onkeypress(fun=tiltRight, key="d")
screen.onkey(key="c", fun=clearScreen)
screen.exitonclick()
