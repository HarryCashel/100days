import time
from snake import Snake
from turtle import Screen
from food import Food

# Set up screen properties
screen = Screen()
screen.setup(800, 800)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)
# Create our objects
snake = Snake()
food = Food()

# Listen for key presses and perform associated function
screen.listen()
screen.onkeypress(snake.up, "Up")
screen.onkeypress(snake.down, "Down")
screen.onkeypress(snake.left, "Left")
screen.onkeypress(snake.right, "Right")

# Set conditional for game loop
game_on = True

# Our game loop
while game_on:
    screen.update()
    time.sleep(.1)
    snake.move_body()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.add_piece()


screen.exitonclick()
