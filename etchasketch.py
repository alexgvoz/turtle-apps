from turtle import Turtle
from random import choice

COLORS = ["dark slate gray", "dark slate blue", "cadet blue", "sea green", "dark khaki", "tomato4", "SlateBlue2",
          "RoyalBlue4"]
tim = None


def start(screen):
    global tim
    tim = Turtle()

    screen.colormode(255)
    screen.title("Etch A Sketch")

    tim.shapesize(2)
    tim.pensize(5)
    tim.fillcolor("dark slate gray")

    screen.listen()
    screen.onkey(fun=moveForwards, key="w")
    screen.onkey(fun=moveBack, key="s")
    screen.onkeypress(fun=tiltLeft, key="a")
    screen.onkeypress(fun=tiltRight, key="d")
    screen.onkey(key="c", fun=clearScreen)

    screen.exitonclick()


def moveForwards():
    tim.pencolor(choice(COLORS))
    tim.forward(30)


def moveBack():
    tim.pencolor(choice(COLORS))
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
