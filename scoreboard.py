import turtle
from turtle import Turtle
class Scoreboard:

    def __init__(self):
        self.score1=0
        self.high_score=0
        self.score=turtle.Turtle()
        self.score.pencolor("white")
        self.score.fillcolor("white")
        self.score.hideturtle()
        self.score.penup()
        self.score.goto(x=-280,y=250)
        self.file=open("high.txt","r+")
        self.max_score=self.file.read()


    def update_score(self):
        self.score1+=1

    def write_score(self):
        self.score.clear()
        self.score.write(arg=f"score = {self.score1}   high score = {self.high_score}")

    def update_highscore(self):
        if self.score1>self.high_score:
            self.high_score=self.score1
            self.file.write(str(self.high_score))

    def reset_score(self):
        self.score1=0

    def check_highscore(self):
        self.high_score=int(self.file.read())


