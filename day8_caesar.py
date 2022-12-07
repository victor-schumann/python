# --- functions ---

#Encrypt
    #Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(text, shift, alphabet):
    caesar = []
    message = [x for x in text]
    for letter in message:
        if letter == ' ':
            caesar.append(' ')
        
        elif letter in alphabet:
            index = alphabet.index(letter)
            ##🐛Bug alert: What happens if you try to encode 'z'?
            if index+shift < 26:
                caesar.append(alphabet[index+shift])
            else:
                caesar.append(alphabet[index+shift-26])
    return caesar

def decrypt(text, shift, alphabet):
    caesar = []
    message = [x for x in text]
    for letter in message:
        if letter == ' ':
            caesar.append(' ')
        
        elif letter in alphabet:
            index = alphabet.index(letter)
            ##🐛Bug alert: What happens if you try to encode 'z'?
            if index+shift < 26:
                caesar.append(alphabet[index+shift])
            else:
                caesar.append(alphabet[index+shift-26])
    return caesar

# --- var declaration ---
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# --- code ---
direction = ''
ask = input("\nType 'E' to encrypt, type 'D' to decrypt (E/D): ").lower()
while direction == '':
    if ask == 'e':
        direction = 'e'
        text = input("\nType your message: ").lower()
        shift = int(input("\nType the shift number: "))

        message = ''.join(encrypt(text, shift, alphabet))
        print(f"\nThe ENCODED message is: \n\n\t{message.upper()}\n")

    elif ask == 'd':
        direction = 'd'
        text = input("\nType your message: ").lower()
        shift = int(input("\nType the shift number: "))

        message = ''.join(decrypt(text, shift, alphabet))
        print(f"The DECODED message is: \n\n\t{message.upper()}\n")

    else:
        print("\nThat is not a valid option. Would you like to try again?")
        direction = input("\nType 'E' to encrypt, type 'D' to decrypt (E/D): ").lower()

#FAQ:
    #https://stackoverflow.com/questions/5618878/how-to-convert-list-to-string

    #https://stackoverflow.com/questions/5453026/string-to-list-in-python

    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list