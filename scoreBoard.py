from  turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self, screen):
        super().__init__()
        self.screen=screen
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score=0
        self.right_score=0
        self.update_score()
    def update_score(self):
        self.clear()
        self.goto((self.screen.window_width()//4,self.screen.window_height()//2-100))
        self.write(self.right_score, align="center", font=("Courier", 60, "normal"))
        self.goto((-self.screen.window_width()//4,self.screen.window_height()//2-100))
        self.write(self.left_score, align="center", font=("Courier", 60, "normal"))
    def add_to_left(self):
        self.left_score+=1
        self.update_score()
    def add_to_right(self):
        self.right_score+=1
        self.update_score()
