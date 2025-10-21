from turtle import Turtle
from random import choice
from time import sleep

class Ball(Turtle):
    SIZE=20
    WIDTH_FACTOR=5
    FASTER = 0.9
    STARTING_SPEED=0.05
    def __init__(self, screen, left_paddle, right_paddle):
        super().__init__(shape="circle")
        self.screen=screen
        self.color("blue")
        self.speed(1)
        self.penup()
        self.xcor_steps=5
        self.ycor_steps=5
        self.left_paddle=left_paddle
        self.right_paddle=right_paddle
        self.paddle_abs_xcor=abs(self.right_paddle.xcor())
        self.ball_speed=self.STARTING_SPEED
    def choose_direction(self):
        self.xcor_steps *= choice([-1, 1]) # choosing random direction for the ball
        self.ycor_steps *= choice([-1, 1])
    def move(self):
        # move
        self.goto(self.xcor() + self.xcor_steps, self.ycor() + self.ycor_steps)
        # check collision with wall
        if abs(self.ycor())>self.screen.window_height()//2 - self.SIZE:
            self.ycor_steps *= -1 # bounce
        # check collision with paddles
        if (((self.distance(self.right_paddle.pos()) < self.WIDTH_FACTOR * self.SIZE) or
             (self.distance(self.left_paddle.pos()) < self.WIDTH_FACTOR * self.SIZE)) and
              abs(self.xcor()) > self.paddle_abs_xcor - 1.25 * self.SIZE):
            self.xcor_steps *= -1 # bounce
            self.ball_speed*=self.FASTER
        sleep(self.ball_speed)
    def reset_ball(self):
        self.ball_speed=self.STARTING_SPEED
        self.goto(0,0)
        self.choose_direction()
