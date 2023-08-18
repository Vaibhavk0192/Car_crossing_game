COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

from turtle import Turtle
import random 


class CarManager():
    def __init__(self) -> None:
        self.all_cars=[]
        self.car_speed=STARTING_MOVE_DISTANCE

    def create_cars(self):
        chance=random.randint(1,8)
        if chance==1:
            new_cars=Turtle("square")
            new_cars.shapesize(stretch_len=2,stretch_wid=1)
            new_cars.penup()
            new_cars.color(random.choice(COLORS))
            random_y=random.randint( -250,250)
            new_cars.goto(300,random_y)
            self.all_cars.append(new_cars)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed+=MOVE_INCREMENT
        






