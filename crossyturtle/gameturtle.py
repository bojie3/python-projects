from turtle import Turtle


class Gameturtle(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color('black')
        self.goto(0, -230)
        self.setheading(90)
        self.shape('turtle')

    def move(self):
        self.forward(20)

    def down(self):
        self.setheading(270)
        self.forward(20)
        self.setheading(90)

    def restart(self):
        self.goto(0, -230)
