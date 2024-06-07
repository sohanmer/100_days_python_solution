print("The Love Calculator is calculating your score...")
name1 = input("What is your name? ") # What is your name?
name2 = input("What is their name? ") # What is their name?

combined_name = (name1 + name2).lower()
true_count = 0
love_count = 0

true_count += combined_name.count('t')
true_count += combined_name.count('r')
true_count += combined_name.count('u')
true_count += combined_name.count('e')

love_count += combined_name.count('l')
love_count += combined_name.count('o')
love_count += combined_name.count('v')
love_count += combined_name.count('e')

total_score = true_count * 10 + love_count

if total_score < 10 or total_score > 90:
  print(f'Your score is {total_score}, you go together like coke and mentos.')
elif total_score > 40 and total_score < 50:
  print(f'Your score is {total_score}, you are alright together.')
else:
  print(f'Your score is {total_score}.')