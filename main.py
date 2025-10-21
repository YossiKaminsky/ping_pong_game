from turtle import Screen
from paddle import Paddle
from otherPaddle import OtherPaddle
from ball import Ball
from scoreBoard import ScoreBoard


screen_obj=Screen()
screen_obj.tracer(0)
screen_obj.setup(width=800, height=600)
screen_obj.bgcolor("black")
screen_obj.title("Ping Pong Game")
scoreBoard_obj=ScoreBoard(screen=screen_obj)
paddle_obj=Paddle(screen=screen_obj, board_xcor=screen_obj.window_width()//2-30)
otherPaddle_obj=OtherPaddle(screen=screen_obj, board_xcor=-(screen_obj.window_width()//2-30))
paddle_obj.move_paddle()
otherPaddle_obj.move_paddle()
ball_obj=Ball(screen=screen_obj,right_paddle=otherPaddle_obj, left_paddle=paddle_obj)
ball_obj.choose_direction()

game_is_on=True
while game_is_on:
    ball_obj.move()
    screen_obj.update()
    if ball_obj.xcor() > screen_obj.window_width()//2:
        scoreBoard_obj.add_to_right()
        ball_obj.reset_ball()
    if ball_obj.xcor() < -(screen_obj.window_width()//2):
        scoreBoard_obj.add_to_left()
        ball_obj.reset_ball()
screen_obj.exitonclick()

