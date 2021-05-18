from turtle import Turtle

ALIGNMENT = "Center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        self.score = 0
        super().__init__()
        self.penup()
        self.color('white')
        self.hideturtle()
        self.goto(0, 300)
        self.update()

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", False, ALIGNMENT, FONT)

    def update(self):
        self.clear()
        self.write(f"Score: {self.score}", False, ALIGNMENT, FONT)

    def add(self):
        self.score += 1
        self.update()
