from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race?Enter a color:"
                                                          " green/yellow/black/red/blue/orange")
colors = ["black", "yellow", "red", "orange", "blue", "green"]
y_position = [-70, -40, -10, 20, 50, 80]
turtle_list = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    turtle_list.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtle_list:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You have won! The wining color is {winning_color}")
            else:
                print(f"You lost the game! The winning color is {winning_color}")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

        
screen.exitonclick()