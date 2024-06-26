from turtle import Turtle, Screen
import random

turtle = Turtle()
turtle.color("red")
screen = Screen()
turtle.pensize(15)
turtle.speed('fastest')

directions = [0, 90, 180, 270]

def random_color():
  r = random.randint(0, 255)
  g = random.randint(0, 255)
  b = random.randint(0, 255)

  return (r, g, b)

for _ in range(500):
  turtle.color(random_color())
  turtle.forward(30)
  turtle.setheading(random.choice(directions))
