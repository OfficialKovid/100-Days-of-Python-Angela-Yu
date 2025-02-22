import random
import streamlit as st

letters = 'abcdefghijklmnopqrstuvwxyz'
symbols = """!@#$%^&*()_+{|}:";'[]<>?/.,"""

numbers = [1,2,3,4,5,6,7,8,9,0]
capital_letters = [letter.upper() for letter in letters]
lower_case_letters = [letter.lower() for letter in letters]
symbols = [symbol for symbol in symbols]

no_of_small_letters = st.text_input("How may small letters: ")
no_of_capital_letters = st.text_input("How many capital letters: ")
no_of_numbers = st.text_input("How many numbers: ")
no_of_symbols = st.text_input("How many symbols: ")

no_of_small_letters = int(no_of_small_letters) if no_of_small_letters else 0
no_of_capital_letters = int(no_of_capital_letters) if no_of_capital_letters else 0
no_of_numbers = int(no_of_numbers) if no_of_numbers else 0
no_of_symbols = int(no_of_symbols) if no_of_symbols else 0

password = []
for _ in range(no_of_small_letters):
    password.append(random.choice(lower_case_letters))
for _ in range(no_of_capital_letters):
    password.append(random.choice(capital_letters))
for _ in range(no_of_numbers):
    password.append(str(random.choice(numbers)))
for _ in range(no_of_symbols):
    password.append(random.choice(symbols))
if st.button("Show Result"):
    random.shuffle(password)
    password = "".join(password)
    st.write("Your Password:")
    st.write(password)
    st.write(f"It is {len(password)} digit long.")

    