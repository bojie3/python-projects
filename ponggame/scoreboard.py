from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.goto(-150, 240)
        self.hideturtle()
        self.shapesize(5, 5)
        self.left_score = 0
        self.right_score = 0
        self.update()

    def update(self):
        self.write(f'{self.left_score}                    {self.right_score}', font=('Arial', 40, 'normal'))

    def update_score(self, side):
        side.lower()
        if side == 'left':
            self.left_score += 1
        else:
            self.right_score += 1
        self.clear()
        self.update()
