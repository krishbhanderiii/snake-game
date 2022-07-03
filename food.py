SHAPE = "circle"
SHAPE_SIZE = 0.5
COLOR = "blue"
from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape(SHAPE)
        self.penup()
        self.shapesize(SHAPE_SIZE, SHAPE_SIZE)
        self.goto(random.randint(-280, 280), random.randint(-280, 280))
        self.speed("fastest")
        self.color(COLOR)

    def Update(self):
        self.goto(random.randint(-280, 280), random.randint(-280, 280))
