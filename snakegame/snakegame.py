from snakegame.snake import Snake


def start(screen):
    screen.setup(600, 600)
    screen.title("Snake Game")
    screen.tracer(0)

    Snake(screen)

    screen.exitonclick()
