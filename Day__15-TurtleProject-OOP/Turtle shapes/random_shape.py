from turtle import Turtle, Screen
import random


tim = Turtle()
tim.shape("turtle")
tim.color("maroon")

colors = ["dark green", "firebrick", "rosy brown", "orange red", "indigo", "slate blue", "spring green",  "black", "red"]


def draw_shape(number_size):
    angle = 360 / number_size
    for _ in range(number_size):
        tim.forward(100)
        tim.right(angle)


for shape_size in range(3, 11):
    tim.color(random.choice(colors))
    draw_shape(shape_size)


screen = Screen()
screen.exitonclick()