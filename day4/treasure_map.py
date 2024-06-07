line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input("Where do you want to put the treasure? ")

x_axis = 0
if position[0] == 'A':
  x_axis = 0
elif position[0] == 'B':
  x_axis = 1
else:
  x_axis = 2

y_axis = int(position[1]) - 1

map[y_axis][x_axis] = 'X'

print(f"{line1}\n{line2}\n{line3}")