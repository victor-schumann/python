# --- functions ---
def cipher(start_text, shift_int, cipher_direction):
    end_text = ""
    if cipher_direction == 'd':
        shift_int *= -1

    for letter in start_text:
        if letter == ' ':
            end_text+=letter
        else:
            position = alphabet.index(letter)
            new_position = position+shift_int
            end_text+=alphabet[new_position]

    print(shift_int)
    print(f"The final message is: \n\t{end_text.upper()}")

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

# --- var declaration ---
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# --- code ---
controlo = 0
while controlo == 0:
    direction = input("\nType 'E' to encrypt, type 'D' to decrypt (E/D): ").lower()

    if direction == 'e' or direction == 'd':
        controlo+=1
        text = input("\nType your message: ").lower()
        shift = int(input("\nType the shift number: "))
        cipher(text, shift, direction)
        
    else:
        controlo=0
        print("\nThat is not a valid option. Would you like to try again?")
        # ask = input("\nType 'E' to encrypt, type 'D' to decrypt (E/D): ").lower()

#FAQ:
    #https://stackoverflow.com/questions/5618878/how-to-convert-list-to-string

    #https://stackoverflow.com/questions/5453026/string-to-list-in-python

    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list