print("Welcome to the Band Name Genrator Program.")

city = input("Enter the name of city you where you grow up? \n")
pet_name = input("Enter the name of your pet?\n")

band_name = city.strip().capitalize() + " " + pet_name.strip().capitalize()

print(f"Your band name could be {band_name}")