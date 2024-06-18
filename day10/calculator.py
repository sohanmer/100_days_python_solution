def add(n1, n2):
  return n1 + n2


def subtract(n1, n2):
  return n1 - n2


def multiply(n1, n2):
  return n1 * n2


def divide(n1, n2):
  return n1 / n2


operations = {"+": add, "-": subtract, "*": multiply, "/": divide}

continue_calculating = 'y'


def calculator():
  num1 = float(input("What's the first number?: "))
  num2 = float(input("What's the second number?: "))
  for op in operations:
    print(op)
  operation = input("Pick a operation from above mentioned lines: ")

  while continue_calculating:
    function = operations[operation]
    result = function(num1, num2)

    print(f'{num1} {operation} {num2} = {result}')
    calculate = input(
        f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: "
    ).lower()
    if calculate == 'y':
      num1 = result
      num2 = float(input("What's the next number?: "))
      operation = input("Pick a operation: ")
    else:
      calculator()


calculator()
