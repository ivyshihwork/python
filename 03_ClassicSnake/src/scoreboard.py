from turtle import Turtle

ALIGNMENT = "Center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        self.score = 0
        self.high_score = 0
        super().__init__()
        self.penup()
        self.color('white')
        self.hideturtle()
        self.goto(0, 300)
        self.update()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"GAME OVER", False, ALIGNMENT, FONT)

    def resetScoreboard(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.update()
        self.score = 0

    def update(self):
        self.clear()
        self.write(f"Score: {self.score}    High Score: {self.high_score}", False, ALIGNMENT, FONT)

    def add(self):
        self.score += 1
        self.update()
