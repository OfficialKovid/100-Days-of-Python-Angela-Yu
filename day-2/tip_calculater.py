print("Welcome to the tip Calculater Program")

bill_amount = float(input("Enter the total amount of the Bill in ₹ "))
tip_percent = float(input("Enter the tip percent: "))
total_no_of_people = int(input("Enter Total number of people: "))


total_payable_amount = bill_amount + (bill_amount * tip_percent) /100

per_person_share = total_payable_amount/total_no_of_people


print(f"Per person share is ₹{per_person_share:.2f} total payable amount ₹{total_payable_amount:.2f}.")
print("Thank you for using our service *^____^* ")
