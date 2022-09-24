from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=1)
        self.color("white")
        self.penup()
        self.xmove=5
        self.ymove=5
    def move(self):
        new_x=self.xcor()+self.xmove
        new_y=self.ycor()+self.ymove
        self.goto(new_x,new_y)
        self.speed(10)
    def bounce_y(self):
        self.ymove*=-1
    def bounce_x(self):
        self.xmove*=-1
    def reset_center(self):
        self.goto(0,0)
        self.xmove*=-1
        self.ymove*=-1
