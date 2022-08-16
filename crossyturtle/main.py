from turtle import Screen
from gameturtle import Gameturtle
from gamecars import Gamecars
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=700, height=500)
screen.tracer(0)
game_icon = Gameturtle()
game_cars = Gamecars()
score = Scoreboard()
screen.update()

screen.onkey(game_icon.move, 'Up')
screen.onkey(game_icon.down, 'Down')
screen.listen()

distance = 10
game_state = True
while game_state:
    screen.update()
    time.sleep(0.1)
    game_cars.create_cars()
    game_cars.move(distance)
    game_cars.maintanence()
    coordinates = game_cars.detect_collision(game_icon.ycor())
    for coordinate in coordinates:
        if abs(game_icon.xcor() - coordinate) < 18:
            game_state = False
            screen.clear()
            score.end_game()
            break
    if game_icon.ycor() > 200:
        screen.clear()
        screen = Screen()
        screen.setup(width=700, height=500)
        screen.tracer(0)
        game_cars.restart()
        distance += 2
        game_icon = Gameturtle()
        score.update_score()
        screen.update()
        screen.onkey(game_icon.move, 'Up')
        screen.onkey(game_icon.down, 'Down')
        screen.listen()
screen.exitonclick()
