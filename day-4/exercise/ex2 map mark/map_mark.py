line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input("Choose from A1-C3: ").capitalize() # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇
import sys
"""
- Mark the sport on map with X
- Map is a 3d array
- position is the input
- B3 where B is coloum and A is row
"""
if position not in ['A1','A2','A3','C1','C2','C3','B1','B2','B3',]:
  print("Wrong input")
  sys.exit()

row = int(position[-1])
coloum = position[0]

if coloum == 'A':
  coloum = 1
elif coloum == 'B':
  coloum = 2
elif coloum == 'C':
  coloum = 3
else:
  print("Unexpected error")

map[row-1][coloum-1] = 'X'



# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")