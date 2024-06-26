from turtle import Turtle, Screen

turtle = Turtle()
turtle.color("red")
screen = Screen()

for _ in range(4):
    turtle.forward(100)
    turtle.right(90)


screen.exitonclick()