from turtle import Turtle

PADDLE_WIDTH_STRETCH = 5
PADDLE_LENGTH_STRETCH = 1


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=PADDLE_WIDTH_STRETCH, stretch_len=PADDLE_LENGTH_STRETCH)
        self.color("white")
        self.penup()
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + 30
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 30
        self.goto(self.xcor(), new_y)
