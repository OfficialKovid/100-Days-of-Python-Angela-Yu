import random

options = ["""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
,
"""
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""
,
"""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""]

users_choice = int(input("Enter 0 = rock, 1 = paper and 2 = scissors: "))
if users_choice not in [0,1,2]:
    print("Invalid input")
    exit()
computers_choice = random.randint(0,2)

if users_choice == computers_choice:
    print("It's a draw")
    print(f"Your choice: {options[users_choice]}")
    print(f"computers choice: {options[computers_choice]}")
elif (users_choice == 0 and computers_choice == 1) or (users_choice == 1 and computers_choice == 2) or (users_choice == 2 and computers_choice == 0):
    print("you lost")
    print(f"your choice {options[users_choice]}")
    print(f"computers choice {options[computers_choice]}")
else:
    print("you win")
    print(f"your choice {options[users_choice]}")
    print(f"computers choice {options[computers_choice]}")