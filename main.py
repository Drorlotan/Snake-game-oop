from turtle import Screen
import time

import score
import snake
import food
import score

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("SNAKE")
screen.tracer(0)
screen.listen()


snake = snake.Snake()
food = food.Food()
points = score.Score()
top_score = score.Score()
top_score.goto(-250,250)
top_score.write(arg=f"high score: {points.highest_score()}", align=("center"))

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    points.write(arg=f"score: {points.score}", align=("center"))
    points.highest_score()

    if snake.head.distance(food) < 15:
        food.refresh()
        points.add_score()
        snake.extend()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 \
        or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        points.game_over()
        game_is_on = False

    if snake.check_tail() == True:
        points.game_over()
        game_is_on = False
screen.exitonclick()
