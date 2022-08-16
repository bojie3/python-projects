from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-320, 200)
        self.color('black')
        self.score = 0
        self.write(f'level {self.score + 1} score {self.score}', font=('Arial', 20, 'normal'))

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f'level {self.score + 1}, score {self.score}', font=('Arial', 20, 'normal'))

    def end_game(self):
        self.clear()
        self.goto(-160, 0)
        self.write(f'game over, your score is {self.score}', font=('Arial', 20, 'normal'))
