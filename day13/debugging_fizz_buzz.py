target = int(input())
for number in range(1, target + 1):
  if number % 3 == 0 and number % 5 == 0: # use "and" instead of "or"
    print("FizzBuzz")
  elif number % 3 == 0: # use elif instead of if
    print("Fizz")
  elif number % 5 == 0: # use elif instead of if
    print("Buzz")
  else:
    print(number) # remove [] brackets