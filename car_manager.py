from turtle import Turtle
from random import randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        choice = randint(1, 6)
        if choice == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.turtlesize(1, 2)
            new_car.penup()
            new_car.color(COLORS[randint(0, len(COLORS) - 1)])
            new_car.left(180)
            new_car.goto(300, randint(-250, 250))
            self.cars.append(new_car)

    def move(self):
        for car in self.cars:
            car.forward(self.car_speed)

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT
