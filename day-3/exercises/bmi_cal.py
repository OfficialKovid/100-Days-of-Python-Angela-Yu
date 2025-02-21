
height = float(input("Enter your height in foot e.g., 5.6 or 6 or 5.85: "))
height = height * 0.3048

weight = int(input("Enter your weight in kilograms e.g., 72: ")) 

bmi = weight / (height ** 2)

if bmi < 18.5:
  print(f"Your BMI is {bmi}, you are underweight.")
elif 18.5 <= bmi < 25:
  print(f"Your BMI is {bmi}, you have a normal weight.")
elif 25 <= bmi < 30:
  print(f"Your BMI is {bmi}, you are slightly overweight.")
elif 30 <= bmi < 35:
  print(f"Your BMI is {bmi}, you are obese.")
elif bmi >= 35:
  print(f"Your BMI is {bmi}, you are clinically obesee.")
else:
  print("Wrong input!")
  