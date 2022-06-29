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

        while game_is_on:
            time.sleep(0.05)
            if player.ycor() > 280:
                player.goToStart()
                scoreboard.update()
                cars.speedUp()

            cars.spawnTurtle()
            cars.moveCars()
            cars.cleanUp()
            screen.update()
            for car in cars.activecars:
                if car.distance(player) < 20:
                    scoreboard.gameOver()
                    game_is_on = False

        screen.exitonclick()
