from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

paddle = Paddle()
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="w", fun=paddle.go_l_up)
screen.onkey(key="s", fun=paddle.go_l_down)
screen.onkey(key="Up", fun=paddle.go_r_up)
screen.onkey(key="Down", fun=paddle.go_r_down)


is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(paddle.r_paddle) < 50 and ball.xcor() > 320 \
            or ball.distance(paddle.l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 370:
        ball.refresh_game()
        scoreboard.l_point()

    if ball.xcor() < -370:
        ball.refresh_game()
        scoreboard.r_point()

screen.exitonclick()
