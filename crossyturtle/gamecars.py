from turtle import Turtle
import random
starting_colors = ['red', 'yellow', 'orange', 'green', 'blue', 'purple']
y_positions = []
for i in range(1, 10):
    y_cor = -210 + i * 40
    y_positions.append(y_cor)


class Gamecars():

    def __init__(self):
        self.cars = []

    def create_cars(self):
        car = Turtle()
        car.penup()
        car.goto(360, random.choice(y_positions))
        car.setheading(180)
        car.shape('square')
        car.color(random.choice(starting_colors))
        self.cars.append(car)

    def move(self, distance):
        for vehicle in self.cars:
            vehicle.forward(distance)

    def maintanence(self):
        if len(self.cars) >= 70:
            counter = 0
            for i in range(len(self.cars) - 1):
                if self.cars[i].xcor() < -360:
                    counter += 1
            self.cars = self.cars[counter:len(self.cars)]

    def detect_collision(self, y_position):
        listx = []
        for vehicle in self.cars:
            if vehicle.ycor() == y_position:
                listx.append(vehicle.xcor())
        return listx

    def restart(self):
        self.cars = []
