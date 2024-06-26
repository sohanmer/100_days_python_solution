from turtle import Turtle, Screen
import random

turtle = Turtle()
turtle.color("red")
screen = Screen()


def random_color():
  r = random.randint(0, 255)
  g = random.randint(0, 255)
  b = random.randint(0, 255)

  return (r, g, b)

def create_shape(side_num):
  turtle.color(random_color())
  angle = 360/side_num
  for _ in range(side_num):
    turtle.forward(100)
    turtle.right(angle)

for side_num in range(3, 11):
	create_shape(side_num)
