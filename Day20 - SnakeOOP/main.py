import time
from snake import Snake
from turtle import Screen
from food import Food


screen = Screen()
screen.setup(800, 800)
screen.bgcolor("black")
screen.title("Snake")

snake = Snake()
food = Food()
screen.listen()

game_on = True

while game_on:
    screen.update()
    time.sleep(.01)
    snake.move_body()
    screen.onkeypress(snake.up, "Up")
    screen.onkeypress(snake.down, "Down")
    screen.onkeypress(snake.left, "Left")
    screen.onkeypress(snake.right, "Right")

screen.exitonclick()
