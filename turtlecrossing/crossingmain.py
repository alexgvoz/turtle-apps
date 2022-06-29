import time
from turtlecrossing.player import Player
from turtlecrossing.car_manager import CarManager
from turtlecrossing.scoreboard import Scoreboard


class TurtleCrossing:

    def start(self, screen):
        screen.setup(600, 600)
        screen.tracer(0)

        game_is_on = True

        scoreboard = Scoreboard()
        player = Player(screen)
        cars = CarManager()
        cars.spawnTurtle()

        while game_is_on:
            time.sleep(0.1)

            screen.update()

        screen.exitonclick()
