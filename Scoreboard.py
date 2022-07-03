from turtle import Turtle

SCORE_COLOR = "black"
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.SCORE = 0
        with open("data.txt") as File:
            self.TEMP =(File.read())
        self.HIGH_SCORE = int(self.TEMP)
        self.color(SCORE_COLOR)
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.SCORE} high Score:{self.HIGH_SCORE}", align=ALIGNMENT, font=FONT)

    def Increase_Score(self):
        self.SCORE = self.SCORE + 1
        self.update_scoreboard()

    def game_over(self):
        if self.SCORE > self.HIGH_SCORE:
            self.HIGH_SCORE = self.SCORE
            with open("data.txt", mode='w') as File:
                File.write(str(self.HIGH_SCORE))
            self.SCORE = 0
            self.update_scoreboard()
