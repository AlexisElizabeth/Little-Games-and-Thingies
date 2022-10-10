from turtle import Turtle, Screen
from random import randint

is_race_on = False

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make Your Bets!",
                            prompt="Which turtle will win the race? Enter a colour in the rainbow: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [80, 50, 20, -10, -40, -70]
all_turtles = []

for turtle_index in range(0,6):
    new_turtle = Turtle("turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-220, y=y_position[turtle_index])
    all_turtles.append(new_turtle)

print(all_turtles)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print("You won!")
            else:
                print("You lost")
        rand_distance = randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
