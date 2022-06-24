import time

from snakegame.food import Food
from snakegame.snake import Snake
from snakegame.scoreboard import Scoreboard


def start(screen):
    screen.setup(600, 600)
    screen.title("Snake Game")
    screen.tracer(0)

    game_is_on = True

    snake = Snake(screen)
    food = Food()
    scoreboard = Scoreboard()

    while game_is_on:
        screen.update()
        time.sleep(0.05)
        snake.move()

        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            scoreboard.updateScore()

        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
            scoreboard.gameOver()
            game_is_on = False

        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 5:
                game_is_on = False
                scoreboard.gameOver()
                break

    screen.exitonclick()
