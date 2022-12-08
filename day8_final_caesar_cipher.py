from support import alphabet, numbers, symbols, logo

#FAQ:
    #https://stackoverflow.com/questions/5618878/how-to-convert-list-to-string

    #https://stackoverflow.com/questions/5453026/string-to-list-in-python

    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

#GOALS
    #This program attempts to optimize 'day_caesar3.py' using while loops and library functions.

    #The user inputs a character, a number, and a message, and the program encrypts or decrypts it based on the famous caesar cipher.

    #The program takes in consideration different user inputs, as well as possible misunderstandings.

#FUNCTIONS
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

#CODE
controlo = 0
encoded_num = 0
direction = ''

while not direction.isalpha():
    should_end = False

    while not should_end:
        print(logo)
        print(f"\nProcessed messages: {encoded_num}")
        direction = input("\nType 'E' to encrypt, type 'D' to decrypt (E/D): ").lower()

        if direction == 'e' or direction == 'd':
            text = input("Type your message: ").lower()
            shift = ''
            
            while not shift.isnumeric():
                shift = input("Type a valid shift number: ")

            if int(shift)>=26:
                shift = shift%26
            
            cypher(text, shift, direction)
            encoded_num+=1
        
            restart = input("\nWould you like to RESTART the program? (y/N): ").lower()

            if restart == 'n' or restart == '':
                should_end = True
                print("\nGoodbye!")
        else:
            print("\nThat is not a valid option. Try again!")
