from turtle import Screen
import time
from food import Food
from Snake import Snake
from Scoreboard import Scoreboard

BG_COLOR = "white"

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor(BG_COLOR)
screen.title("WELCOME TO SNAKE GAME?")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.Up, "Up")
screen.onkey(snake.Down, "Down")
screen.onkey(snake.Left, "Left")
screen.onkey(snake.Right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.Mov()
    # eat food
    if snake.Head().distance(food) < 15:
        food.Update()
        scoreboard.Increase_Score()
        snake.extend()

    if snake.Check_GOVER():
        scoreboard.game_over()
        snake.Reset()

    for segment in snake.segment:
        if segment == snake.segment[0]:
            pass
        elif snake.Head().distance(segment) < 15:
            scoreboard.game_over()
            snake.Reset()
screen.exitonclick()
