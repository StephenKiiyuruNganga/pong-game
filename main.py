import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Turtle Crossing")

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=player.move, key="Up")

game_is_on = True
loop_count = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()
    loop_count += 1

    if loop_count == 6:
        car_manager.create_car()
        loop_count = 0

    car_manager.move_cars()

    # detect collision with car
    for car in car_manager.cars:
        if player.distance(car) < 30:
            game_is_on = False
            scoreboard.game_over()

    # detect if player crossed successfully
    if player.has_finished():
        player.restart()
        car_manager.increase_speed()
        scoreboard.increase_level()

screen.exitonclick()
