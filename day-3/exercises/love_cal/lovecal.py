print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?


both_name = (name1 + name2).lower()

t = both_name.count('t')
r = both_name.count('r')
u = both_name.count('u')
e = both_name.count('e')
true_count = str(t+r+u+e)

l = both_name.count('l')
o = both_name.count('o')
v = both_name.count('v')
e = both_name.count('e')
love_count = str(l+o+v+e)

love_score = int(true_count + love_count)


if  10 > love_score or love_score> 90:
  print(f"Your score is {love_score}, you go together like coke and mentos.")
elif 40 < love_score < 50:
  print(f"Your score is {love_score}, you are alright together.")
else:
  print(f"Your score is {love_score}.")

