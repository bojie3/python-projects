from turtle import Screen
from slider import Slider
from ball import Ball
from scoreboard import Scoreboard
import time

LEFT = (-350, 0)
RIGHT = (350, 0)
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong Game')
screen.tracer(0)

game_ball = Ball()
left_slider = Slider(LEFT)
right_slider = Slider(RIGHT)
middle_slider = Slider((0, 0))
middle_slider.shapesize(stretch_wid=100, stretch_len=0.1)
score = Scoreboard()

screen.onkey(left_slider.up, 'w')
screen.onkey(left_slider.down, 's')
screen.onkey(right_slider.up, 'Up')
screen.onkey(right_slider.down, 'Down')
screen.listen()
game_state = True
counter = 0
while game_state:
    if counter <= 25:
        game_ball.update_speed(counter)
    screen.update()
    game_ball.move()
    time.sleep(0.04)
    if abs(game_ball.ycor()) > 290:
        game_ball.bounce_wall()
    if game_ball.distance(left_slider) < 53.452 or game_ball.distance(right_slider) < 53.452:
        if abs(game_ball.xcor()) > 330:
            game_ball.paddle_collision()
            if game_ball.xcor() > 0:
                score.update_score('right')
            else:
                score.update_score('left')

    if abs(game_ball.xcor()) > 390:
        game_state = False


screen.exitonclick()
