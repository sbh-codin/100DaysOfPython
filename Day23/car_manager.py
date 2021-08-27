from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.all_cars=[]
        self.hideturtle()

    def create(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            newCar = Turtle()
            newCar.shape("square")
            newCar.color(random.choice(COLORS))
            newCar.shapesize(1,2)
            newCar.penup()
            randomY = random.randint(-250,250)
            newCar.goto(300,randomY)
            self.all_cars.append(newCar)

    def move(self):
        for car in self.all_cars:
            car.backward(MOVE_INCREMENT)
        

