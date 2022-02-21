from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,250)
        self.high_score = 0

    def add_score(self):
        self.clear()
        self.score += 1
        self.write(arg=f"score: {self.score}", align=("center"))

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER")

    def highest_score(self):
        with open("data.txt", "r") as data:
            top_score = int(data.read())
        if self.score > top_score:
            with open("data.txt", "w") as data:
                data.write(str(self.score))
        return top_score