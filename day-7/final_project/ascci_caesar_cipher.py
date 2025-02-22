import streamlit as st
import sys

def check_input_validity(user_input,data_type:type, inner_text, expected_input:list,):
    if expected_input:
        wrong_input_count = 0
        while user_input not in expected_input:
            if wrong_input_count >= 10:
                print("Multiple Wrong attempt")
                print("Exited")
                sys.exit()
            print("Wrong input try again! ")
            user_input = data_type(input(inner_text))   
            wrong_input_count += 1
        return user_input
    return user_input


def take_valid_input(inner_text:str,data_type:type,expected_input:list=None,):
    wrong_input_count = 0
    while True:
        try:
            user_input = input(inner_text).strip().lower()
            user_input = data_type(user_input)
            if expected_input:
                # print("Expected input is ", expected_input)
                user_input = check_input_validity(user_input,data_type,inner_text,expected_input)
            return user_input
        except ValueError:
            if wrong_input_count >= 10:
                print("Multiple Wrong attempt")
                print("Exited")
                sys.exit()
            print(f"Invalid input the input must be of type {data_type}")
            wrong_input_count += 1
            
        except Exception as e:
            if wrong_input_count >= 10:
                print("Multiple Wrong attempt")
                print("Exited")
                sys.exit()
            print(f"Invalid input{e}")
            wrong_input_count +=1
            
    
def encode():
    data = take_valid_input("What you want to encode:\n",str)
    expected_shift_input = [x for x in range(1,101)]
    shift_count = take_valid_input(inner_text="What will be the shift count [1-100]: ",\
                                    data_type=int,\
                                    expected_input=expected_shift_input)
    print(f"{data}, {shift_count}")
    encoded_data = ''
    for i in data:
        encoded_data += chr(ord(i) + shift_count)
    print(f"The encoded data: {encoded_data}")
    
    
def decode():
    expected_shift_input = [x for x in range(1,101)]
    data = input("Enter encrypted data: ")
    shift = take_valid_input("Enter the shift value [1-100]: ",int,expected_shift_input)
    decoded_data = ''
    for i in data:
        decoded_data += chr(ord(i) - shift)
    print(f"The decode data: {decoded_data}")


if __name__ == "__main__":
    while True:
        user_input_choice = take_valid_input("Choose 'encode' or 'decode' or 'exit': ",str,['encode','decode','exit'])
        if user_input_choice == 'encode':
            encode()
        elif user_input_choice == 'decode':
            decode()
        elif user_input_choice.lower() == 'exit':
            sys.exit()
        else:
            print("Wrong input")