from turtle import Turtle, done


FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.level = 0
        self.hideturtle()
        self.update()

    def increase(self):
        self.level += 1
        self.update()

    def update(self):
         self.clear()
         self.penup()
         self.hideturtle()
         self.goto(-20,250)
         self.write(self.level, align= "center", font=FONT)

    def gameOver(self):
        self.goto(0,0)
        self.write("Game Over!", align= "center", font=FONT)