import random
from turtle import Turtle
from turtle import Screen

turtle = Turtle()
screen = Screen()
turtle.speed(0) # 1:slowest, 3:slow, 5:normal, 10:fast, 0:fastest
turtle.penup()
colors = [(232, 230, 227), (233, 228, 231), (231, 236, 233), (230, 232, 236), (199, 158, 116), (157, 85, 39), (42, 107, 150), (132, 168, 188), (191, 155, 21), (10, 28, 60), (193, 142, 163), (149, 64, 93), (62, 24, 10), (63, 16, 36), (156, 25, 10)]

def random_color():
  return random.choice(colors)

turtle.setheading(225)
turtle.forward(250)
turtle.setheading(0)

for _ in range(10):
  for _ in range (10):
    turtle.dot(10, random_color())
    turtle.forward(30)

  turtle.left(90)
  turtle.forward(30)
  turtle.left(90)
  turtle.forward(300)
  turtle.right(180)

