from turtle import Screen
from ball import Ball
from paddle import Paddle
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(1000, 600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.listen()
screen.tracer(0)

paddle1 = Paddle((450, 0))
paddle2 = Paddle((-450, 0))


def key_binding(paddle, string1_binding, string2_binding):
    screen.onkey(paddle.up, string1_binding)
    screen.onkey(paddle.down, string2_binding)


key_binding(paddle1, "Up", "Down")
key_binding(paddle2, "w", "s")

ball = Ball()
score=Scoreboard()

is_game_on = True
while is_game_on:
    time.sleep(0.02)
    screen.update()
    ball.move()
    if ball.ycor()>289 or ball.ycor()<-289:
        ball.bounce_y()
    if ball.distance(paddle1)<50 and ball.xcor()>429:
        ball.bounce_x()

    if ball.distance(paddle2)<50 and ball.xcor()<-429:
        ball.bounce_x()

    if ball.xcor()>450:
        ball.reset_center()
        score.score1_increase()
  
    if ball.xcor()<-450:
        ball.reset_center()
        score.score2_increase()


screen.exitonclick()
