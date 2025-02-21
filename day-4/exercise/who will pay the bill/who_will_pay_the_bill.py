import streamlit as st
import random

names = st.text_area("Enter names (one per line):").split("\n")

if st.button("Pick Who Pays") and names:
    names = [name.strip() for name in names if name.strip()]  
    if names:
        will_pay_the_bill = random.choice(names)
        st.write(f"{will_pay_the_bill} is going to buy the meal today!")
