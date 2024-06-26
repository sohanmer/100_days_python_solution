from turtle import Turtle, Screen

turtle = Turtle()
turtle.color("red")
screen = Screen()

for _ in range(10):
    turtle.pendown()
    turtle.forward(10)
    turtle.penup()
    turtle.forward(10)
