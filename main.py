from turtle import Screen

from simpleapps import etchasketch, turtlerace
import snakegame.snakegame as snake

if __name__ == "__main__":
    screen = Screen()
    screen.setup(1000, 1000)
    screen.title("Turtle Apps")
    screen.bgcolor("#333333")

    while screen:
        user_input = screen.textinput("", "What game would you like to play?")

        if user_input:
            match user_input.lower():
                case "race":
                    turtlerace.start(screen)
                    break
                case "sketch":
                    etchasketch.start(screen)
                    break
                case "snake":
                    snake.start(screen)
                    break
                case _:
                    print("Please select an existing game.")
        else:
            quit()