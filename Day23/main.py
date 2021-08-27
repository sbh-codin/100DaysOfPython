import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
scoreboard = Scoreboard()
car = CarManager()

screen.listen()
screen.onkey(player.go_up,"Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create()
    car.move()
    if player.ycor()>= 280:
        player.reset()
        scoreboard.increase()
    #if the distance between any of the cars 
    # and player is less that 5 then change gameIsOn to False 
    # and write gameOver
    for carC in car.all_cars:
        if carC.distance(player)<20:
            game_is_on = False
            scoreboard.gameOver()
screen.exitonclick()