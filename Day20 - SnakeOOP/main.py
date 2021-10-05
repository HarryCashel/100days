import time
from snake import Snake
from turtle import Screen

screen = Screen()
screen.setup(800, 800)
screen.bgcolor("black")
screen.title("Snake")

snake = Snake()

screen.listen()

while True:
    screen.update()
    time.sleep(.01)
    snake.move_body()
    screen.onkeypress(snake.move_left, "Left")

exitonclick()
