from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.

print(logo)
print('Welcome to secret auction program.')
more_bidders = True
bids = {}

def find_highest_bidder(bids):
  clear()
  highest_bid = 0
  winner = ''
  for bidder in bids:
    if bids[bidder] > highest_bid:
      highest_bid = bids[bidder]
      winner = bidder

  print(f'The winner is {winner} with a bid of ${highest_bid}')

while more_bidders:
  name = input('What is your name?: ')
  bid = int(input('What is your bid?: $'))
  bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")
  bids[name] = bid
  if bidders == 'yes':
    clear()
  else:
    more_bidders = False

find_highest_bidder(bids)
