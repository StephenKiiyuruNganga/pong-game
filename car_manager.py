import random
from turtle import Turtle


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        self.cars = []
        self.current_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        new_car = Turtle()
        new_car.color(random.choice(COLORS))
        new_car.shape("square")
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.penup()
        new_car.setheading(180)
        new_car.goto(x=300, y=random.randint(-240, 240))
        self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            car.forward(self.current_speed)

    def increase_speed(self):
        self.current_speed += MOVE_INCREMENT
