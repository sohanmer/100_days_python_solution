# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

total_student = 0
total_height = 0
# Calculating height without using count or len function
for height in student_heights:
  total_student += 1
  total_height += height

print(f'total height = {total_height}')
print(f'number of students = {total_student}')
print(f'average height = {round(total_height/total_student)}')
