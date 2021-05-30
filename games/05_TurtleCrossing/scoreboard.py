from turtle import Turtle

ALIGNMENT = "left"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 1
        self.goto(x, y)
        self.update()

    def update(self):
        self.write(f"Level = {self.level}", False, ALIGNMENT, FONT)

    def add(self):
        self.level += 1
        self.clear()
        self.update()

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"GAME OVER", False, "center", ("Courier", 48, "bold") )
        self.goto(-280,250)
        self.update()
