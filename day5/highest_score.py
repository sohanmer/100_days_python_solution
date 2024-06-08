# Input a list of student scores
student_scores = input().split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

highest_score = 0
# Finding highest score without using max or min function
for score in student_scores:
  if highest_score < score:
    highest_score = score

print(f'The highest score in the class is: {highest_score}')
