import turtle
from turtle import Turtle
from random import randrange

COLORS = ["red", "orange", "yellow", "green", "purple", "blue"]
turtles = []
race_is_on = False


def spawnTurtles():
    for i in range(len(COLORS)):
        turtles.append(Turtle("turtle"))
        turtles[i].color(COLORS[i])
        turtles[i].penup()
        turtles[i].goto(-turtle.screensize()[0], 100 - (i * 40))


def drawFinish():
    tim = Turtle()
    tim.hideturtle()
    tim.penup()
    tim.speed(0)
    tim.goto(turtle.screensize()[0], 200)
    tim.pendown()
    tim.pensize(2)
    tim.right(90)

    for i in range(40):
        if i % 2 == 0:
            tim.pencolor("gray66")
        else:
            tim.pencolor("gray17")

        tim.forward(10)


def start(screen):
    global race_is_on

    screen.title("Turtle Race")

    while True:
        user_bet = screen.textinput("", "Which turtle will win the race? Enter a color: ")

        if user_bet:

            if user_bet in COLORS:
                race_is_on = True
                break
            else:
                print("Please select a valid color.")

        else:
            quit()

    drawFinish()
    spawnTurtles()

    while race_is_on:
        for t in turtles:
            if t.xcor() <= turtle.screensize()[0]:
                t.forward(randrange(0, 10))
            else:
                race_is_on = False

                if user_bet == t.color()[0]:
                    print(f"You've won! The {t.color()[0]} turtle finished first!")
                else:
                    print(f"You've lost! The {t.color()[0]} turtle finished first!")

                break

    screen.exitonclick()
