import random
from art import logo, vs
from game_data import data
from replit import clear


def choose_opponent(data):
  opponent1 = random.choice(data)
  data.remove(opponent1)
  opponent2 = random.choice(data)
  return [opponent1, opponent2]

def compare(opponent1, opponent2):
  if opponent1['follower_count'] > opponent2['follower_count']:
    return 'A'
  else:
    return 'B'

def play():
  print(logo)
  score = 0
  is_correct_answer = True
  while is_correct_answer:
    opponents = choose_opponent(data)
    print(
        f"Compare A: {opponents[0]['name']}, a {opponents[0]['description']}, from {opponents[0]['country']}"
    )
    print(vs)
    print(
        f"Compare B: {opponents[1]['name']}, a {opponents[1]['description']}, from {opponents[1]['country']}"
    )
    user_answer = input("Who has more followers? Type 'A' or 'B': ")
    clear()
    print(logo)
    if user_answer == compare(opponents[0], opponents[1]):
      score += 1
      print(f"You're right! Current score: {score}")
    else:
      print(f"Sorry, that's wrong. Final score: {score}")
      is_correct_answer = False

play()