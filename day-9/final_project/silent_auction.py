import os
from ascii_arts import hammer_logo, winner_logo
bids = {}

def take_input():
    name = input("Enter your name: ")
    bid = int(input("Enter the bid value: "))
    bids[name] = bid
    
def find_winner():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(winner_logo)
    highest_bid = 0
    winner = ""
    for key, value in bids.items():
        if highest_bid < value:
            highest_bid = value
            winner = key
            
            
    print(f"The winner is {winner} his bid was {bids[winner]}")
    
os.system('cls' if os.name == 'nt' else 'clear')
print(hammer_logo)
take_input()
while True:
    add_another = input("If there are more bids then type 'yes' or type 'no': ")
    if add_another == 'yes':
        os.system('cls' if os.name == 'nt' else 'clear')
        print(hammer_logo)
        take_input()
    else:
        break
find_winner()