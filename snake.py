from turtle import Turtle
import random

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
ANGLES = [0, 90, 180, 270]


class Snake:

    def __init__(self):
        self.growing_snake = []
        self.create_snake()
        self.head = self.growing_snake[0]
        self.head.setheading(random.choice(ANGLES))

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_snake(position)

    def add_snake(self, position):
        new_snake = Turtle("square")
        new_snake.color("white")
        new_snake.penup()
        new_snake.goto(position)
        self.growing_snake.append(new_snake)

    def reset(self):
        for part in self.growing_snake:
            part.goto(1000, 1000)
        self.growing_snake.clear()
        self.create_snake()
        self.head = self.growing_snake[0]
        self.head.setheading(random.choice(ANGLES))

    def extend(self):
        self.add_snake(self.growing_snake[-1].position())

    def move(self):
        for snake_num in range(len(self.growing_snake) - 1, 0, - 1):
            new_x = self.growing_snake[snake_num - 1].xcor()
            new_y = self.growing_snake[snake_num - 1].ycor()
            self.growing_snake[snake_num].goto(new_x, new_y)
        self.growing_snake[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
