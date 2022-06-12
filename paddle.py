import turtle
from turtle import Turtle

L_PADDLE = (-350, 0)
R_PADDLE = (350, 0)
positions = [L_PADDLE, R_PADDLE]


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.paddles = []
        self.create_paddle()
        self.l_paddle = self.paddles[0]
        self.r_paddle = self.paddles[1]

    def create_paddle(self):
        for position in positions:
            self.add_paddle(position)

    def add_paddle(self, position):
        new_paddle = Turtle("square")   # create a new object everytime it is called.
        # Since we need multiple objects to be formed and not one.
        new_paddle.color("white")
        new_paddle.penup()
        new_paddle.shapesize(stretch_len=5, stretch_wid=1)
        new_paddle.setheading(90)
        new_paddle.goto(position)
        self.paddles.append(new_paddle)

    def go_l_up(self):
        # self.l_paddle.goto(-350, self.l_paddle.ycor() + 10)
        self.l_paddle.setheading(90)
        self.l_paddle.forward(20)

    def go_l_down(self):
        self.l_paddle.setheading(270)
        self.l_paddle.forward(20)

    def go_r_up(self):
        self.r_paddle.setheading(90)
        self.r_paddle.forward(30)

    def go_r_down(self):
        self.r_paddle.setheading(270)
        self.r_paddle.forward(30)

