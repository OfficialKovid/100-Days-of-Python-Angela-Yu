import time

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

wrong_input_count = 0
while True:
    if wrong_input_count >= 10:
        print("Multiple Wrong input Try again after some time")
        raise Exception("More Then 10 wrong input attempt")
        
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").strip().lower()
    if direction in ['encode','decode']:
        
        break
    print("Wrong Input Try again")
    wrong_input_count += 1
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encode(text,shift):
    encoded_text = ''
    for letter in text:
        if letter in alphabet:
            initial_value_index = alphabet.index(letter)
            if initial_value_index + shift >= len(alphabet):
                 
                difference = (initial_value_index +shift) - len(alphabet)
                difference = difference % 26
                # Not Recommended use %
                # If we encode kovid we will get ycjwr
                # The below program will take 11.572399616241455 seconds
                # while not difference <= 25:
                #     difference -= len(alphabet)
                #     print(difference)
            
                encoded_text += alphabet[difference]
            else:
                encoded_letter = alphabet[initial_value_index + shift]
                encoded_text += encoded_letter
        else:
            encoded_text += letter
        
    print(f"The encoded message is {encoded_text}")
    
def decode(text, shift):
    decoded_text = ''
    for letter in text:
        if letter in alphabet:
            new_index = (alphabet.index(letter) - shift) % 26
            decoded_text += alphabet[new_index]
        else:
            decoded_text += letter
    print(decoded_text)

if __name__ == '__main__':
    start_time = time.time()
    if direction == 'encode':
        encode(text,shift)
    elif direction == 'decode':
        decode(text,shift)
    else:
        print("Wrong input")
    end_time = time.time()
    print(f"the total time {end_time - start_time}")