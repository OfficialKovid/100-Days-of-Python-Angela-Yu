import time
import streamlit as st

alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)]
if "wrong_input_count" not in st.session_state:
    st.session_state.wrong_input_count = 0
    
    
st.title("Caesar Cipher")

direction = st.radio("Choose an option:", ["Encode", "Decode"])
text = st.text_input("Enter your message:").lower()
shift = st.number_input("Enter the shift value:", max_value=10_00_000_00_00_000,value=0, step=1)


shift = shift % 26


def encode(text, shift):
    encoded_text = ''
    for letter in text:
        if letter in alphabet:
            new_index = (alphabet.index(letter) + shift) % 26
            encoded_text += alphabet[new_index]
        else:
            encoded_text += letter
    return encoded_text


def decode(text, shift):
    decoded_text = ''
    for letter in text:
        if letter in alphabet:
            new_index = (alphabet.index(letter) - shift) % 26
            decoded_text += alphabet[new_index]
        else:
            decoded_text += letter
    return decoded_text


if st.button("Run"):
    start_time = time.time()

    if direction.lower() == "encode":
        result = encode(text, shift)
        st.success(f"Encoded message: {result}")
    elif direction.lower() == "decode":
        result = decode(text, shift)
        st.success(f"Decoded message: {result}")
    else:
        st.error("Invalid input.")

    end_time = time.time()
    st.write(f"Total execution time: {end_time - start_time:.5f} seconds")
