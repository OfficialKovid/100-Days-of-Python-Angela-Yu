
def addition(num1,num2):
    """Taka 2 number and return thair addition"""
    return num1 + num2

def substraction(num1:float, num2:float):
    """Take two numbers as input and return its subtraction.

    Args:
        num1 (float): first number
        num2 (float): second number

    Returns:
        float: substration of num1 and num2
    """
    return num1 - num2

def multiplication(num1,num2):
    return num1 * num2

def division(num1, num2):
    return num1 / num2

continue_program = True

while continue_program:
    num1 = float(input("Enter the First number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Select the opration \n+\n-\n*\n/\n").strip().lower()
    
    if operation == '+':
        answer = addition(num1,num2)
    elif operation == '-':
        answer = substraction(num1,num2)
    elif operation == '*':
        answer = multiplication(num1,num2)
    elif operation == '/':
        answer = division(num1,num2)
    else:
        print("Wrong operation input")
    if answer:
        print(f"{num1} {operation} {num2} = {round(answer)}")
    
    want_to_continue = input("Do you want to perform some more operations 'yes' or 'no': ").strip().lower()
    if want_to_continue == 'no':
        print("Bye")
        continue_program = False
    