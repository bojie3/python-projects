from turtle import Turtle


class Slider(Turtle):

    def __init__(self, position):
        super().__init__()
        self.penup()
        self.shape('square')
        self.color('white')
        self.goto(position)
        self.shapesize(stretch_wid=5, stretch_len=1)

    def up(self):
        new_ycor = self.ycor() + 20
        self.goto(self.xcor(), new_ycor)

    def down(self):
        new_ycor = self.ycor() - 20
        self.goto(self.xcor(), new_ycor)
