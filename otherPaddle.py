from paddle import Paddle

class OtherPaddle(Paddle):
    def __init__(self, screen, board_xcor):
        self.screen=screen
        super().__init__(self.screen, board_xcor)
    def move_paddle(self):
        self.screen.listen()
        self.screen.onkey(key="w", fun=self.move_up)
        self.screen.onkey(key="s", fun=self.move_down)

