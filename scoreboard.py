from tkinter import CENTER
from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score1=0
        self.score2=0
        self.goto(0,240)
        self.screen_write()
    def score1_increase(self):
        self.undo()
        self.score1+=1
        self.screen_write()
    def score2_increase(self):
        self.undo()
        self.score2+=1
        self.screen_write()
    def screen_write(self):
        self.write(f"{self.score1}        {self.score2}",align=CENTER,font=["CHEDROS",35,"normal"])

