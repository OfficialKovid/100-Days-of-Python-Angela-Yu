import streamlit as st


st.title("ASCII Caesar Cipher Encoder & Decoder")

def take_valid_input(inner_text, data_type, expected_input=None):
    user_input = st.text_input(inner_text) if data_type == str else st.number_input(inner_text, min_value=1, max_value=100, step=1)
    
    if expected_input and user_input not in expected_input:
        st.error(f"Invalid input! Expected: {expected_input}")
        return None
    return user_input


def encode(data, shift_count):
    encoded_data = ''.join(chr(ord(i) + shift_count) for i in data)
    return encoded_data


def decode(data, shift):
    decoded_data = ''.join(chr(ord(i) - shift) for i in data)
    return decoded_data


operation = st.radio("Choose an operation:", ["Encode", "Decode"])
data = st.text_input("Enter the text:")
shift = st.number_input("Enter shift count:", min_value=1, max_value=100, step=1)

if st.button("Run"):
    if operation == "Encode":
        result = encode(data, shift)
        st.success(f"Encoded Text: {result}")
    elif operation == "Decode":
        result = decode(data, shift)
        st.success(f"Decoded Text: {result}")
