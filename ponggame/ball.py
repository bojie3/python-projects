from turtle import Turtle
import random


def random_func():
    return random.choice(
        (random.randint(0, 45), random.randint(135, 180), random.randint(180, 225), random.randint(315, 360)))


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.speed_level = 5
        self.speed(self.speed_level)
        self.shape('circle')
        self.color('white')
        self.angle = random_func()
        self.update()

    def update(self):
        self.setheading(self.angle)

    def move(self):
        self.forward(10)

    def bounce_wall(self):
        if self.angle == 0 or self.angle == 180:
            return
        else:
            angle = 360 - self.angle
            self.angle = angle
            self.update()

    def paddle_collision(self):
        if self.heading() <= 180:
            angle = 180 - self.angle
            self.angle = angle
            self.update()
        else:
            angle = 540 - self.angle
            self.angle = angle
            self.update()

    def update_speed(self, counter):
        self.speed_level += counter/5
        self.speed(self.speed_level)
