import random
from turtle import Turtle
from turtle import Screen

turtle = Turtle()
screen = Screen()
turtle.speed(0) # 1:slowest, 3:slow, 5:normal, 10:fast, 0:fastest

def random_color():
  r = random.randint(0, 255)
  g = random.randint(0, 255)
  b = random.randint(0, 255)
  
  return (r, g, b)

def draw_spirograph(size_of_gaps):
  for _ in range(int(360 / size_of_gaps)):
    turtle.color(random_color())
    turtle.circle(100)
    turtle.setheading(turtle.heading() + size_of_gaps)
    
draw_spirograph(5)