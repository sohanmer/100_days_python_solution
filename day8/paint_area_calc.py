import math

def paint_calc(height, width, cover):
  area = height * width
  num_of_cans = area/cover
  print(f"You'll need {math.ceil(num_of_cans)} cans of paint.")

# Define a function called paint_calc() so the code below works.   

test_h = int(input()) # Height of wall (m)
test_w = int(input()) # Width of wall (m)
coverage = 5
paint_calc(height=10, width=5, cover=coverage)
