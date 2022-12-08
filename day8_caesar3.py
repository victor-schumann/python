#FAQ:
    #https://stackoverflow.com/questions/5618878/how-to-convert-list-to-string

    #https://stackoverflow.com/questions/5453026/string-to-list-in-python

    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list
from support import alphabet, numbers, symbols, logo

# --- functions ---
def cypher(start_text, shift_int, cipher_direction):
    shift_int = int(shift_int)
    end_text = ""
    if cipher_direction == 'd':
        shift_int *= -1

    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position+shift_int
            end_text+=alphabet[new_position]

        else:
            end_text += char

        # if char in numbers or char in symbols:
        #     end_text+=char

        # else:
        #     position = alphabet.index(char)
        #     new_position = position+shift_int
        #     end_text+=alphabet[new_position]

    print(f"\nThe final message is: {end_text.upper()}")

def encrypt(text, shift, alphabet):
    caesar = ''
    #message = [x for x in text]
    for letter in text:
        if letter == ' ':
            caesar+=letter
        
        elif letter in alphabet:
            position = alphabet.index(letter)
            new_position = position+shift

            if position+shift < 26:
                new_letter = alphabet[new_position]
                caesar+=new_letter

            else:
                new_letter = alphabet[new_position-26]
                caesar+=new_letter

    return caesar

def decrypt(text, shift, alphabet):
    caesar = ''
    for letter in text:
        if letter == ' ':
            caesar+=letter
        
        elif letter in alphabet:
            position = alphabet.index(letter)
            new_position = position-mjshift

            if position+shift < 26:
                new_letter = alphabet[new_position]
                caesar+=new_letter

            else:
                new_letter = alphabet[new_position-26]
                caesar+=new_letter
                
    return caesar

# --- code ---
#TODO: Add big shift numbers support.
#TODO: Createa a while loop to allow the user to use the program again and again.
controlo = 0
encoded_num = 0

#This WHILE's purpose is to verify if the user inputs a valid enconde/decode instruction. To optimize this, we could use a "is letter()" instead.
while controlo == 0:
    should_end = False
# This one is pretty straight forward: it loops the program while the user does not quit it. I was trying to put it above everything, but for some reason I was having difficulties. This while loop must run inside 
    while not should_end:
        print(logo)
        print(f"\nProcessed messages: {encoded_num}")
        direction = input("\nType 'E' to encrypt, type 'D' to decrypt (E/D): ").lower()

        if direction == 'e' or direction == 'd':
            controlo+=1
            text = input("Type your message: ").lower()
#the below experiment proves the above struggle. I want to put the user in a loop whenever he doesn't give me an actual ahift number. To achieve that, I used a simple while loop and the function variable.isnumeric(). I will try to relly more on those functions from other libraries.
            shift = '!'
            while not shift.isnumeric():
                shift = input("Type a valid shift number: ")

            cypher(text, shift, direction)
            encoded_num+=1
        
            restart = input("\nWould you like to RESTART the program? (Y/N): ").lower()

            if restart == 'n':
                should_end = True
                print("\nGoodbye!")
        else:
            controlo=0
            print("\nThat is not a valid option. Try again!")
