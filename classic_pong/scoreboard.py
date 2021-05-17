from turtle import Turtle

ALIGNMENT = "Center"
FONT = ("Courier", 50, "bold")


class Scoreboard(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.lscore = 0
        self.rscore = 0
        self.x = x
        self.y = y
        self.update()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", False, ALIGNMENT, FONT)

    def update(self):
        self.goto(self.x, self.y)
        self.write(f"{self.lscore}", False, ALIGNMENT, FONT)
        self.goto(-self.x, self.y)
        self.write(f"{self.rscore}", False, ALIGNMENT, FONT)

    def addLeft(self):
        self.lscore += 1
        self.clear()
        self.update()

    def addRight(self):
        self.rscore += 1
        self.clear()
        self.update()
