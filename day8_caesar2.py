import support

# --- functions ---
def cipher(start_text, shift_int, cipher_direction):
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

# --- var declaration ---
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = [' ', '!', '#', '$', '%', '&', '(', ')', '*', '+', ',']

# --- code ---
controlo = 0
print(support.caesar)
print(support.cipher)
#TODO: Add big shift numbers support.
#TODO: Createa a while loop to allow the user to use the program again and again.
continue = True
while continue == True:
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
    controlo2 = input("Would you like to TERMINATE the program? (Y/n): ").lower()
    if controlo2 == 'y':
        continue = False
        print("\nGoodbye!")


#FAQ:
    #https://stackoverflow.com/questions/5618878/how-to-convert-list-to-string

    #https://stackoverflow.com/questions/5453026/string-to-list-in-python

    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list