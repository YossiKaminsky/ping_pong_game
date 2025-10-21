from turtle import Turtle, Screen

class Paddle(Turtle):
    SIZE = 20
    def __init__(self, screen, board_xcor):
        super().__init__("square")
        self.screen=screen
        self.penup()
        self.setposition(x=board_xcor,y=0)
        self.color("white")
        self.shapesize(stretch_wid=5,stretch_len=1)
    def move_paddle(self):
        self.screen.listen()
        self.screen.onkey(key="Up", fun=self.move_up)
        self.screen.onkey(key="Down", fun=self.move_down)
    def move_up(self):
        self.goto(self.xcor(), self.ycor() + self.SIZE)
    def move_down(self):
        self.goto(self.xcor(), self.ycor() - self.SIZE)


