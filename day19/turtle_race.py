from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
turtles = {}

height = 100
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "green", "blue", "purple", "yellow"]


for color in colors:
    turtles[color] = Turtle(shape="turtle")
    turtles[color].color(color)
    turtles[color].penup()
    turtles[color].goto(x=-240, y=height)
    height -= 30

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles.values():
        if turtle.pos()[0] >= 230:
            winning_color = turtle.pencolor()
            if user_bet == winning_color:
                print(f"You won! {winning_color} turtle is the winner.")
            else:
                print(f"You lose! {winning_color} turtle is the winner.")
            is_race_on = False
        turtle.forward(random.randint(0, 10))

screen.exitonclick()
