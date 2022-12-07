# --- functions ---
def encrypt(text, shift, alphabet):
    test = []
    for letter in message:
        if letter in alphabet:
            index = alphabet.index(letter)
            test.append(alphabet[index+shift])

# --- var declaration ---
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# --- code ---
#direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
#text = input("Type your message:\n").lower()
text = "fghi"
message = [x for x in text]
print(f"\n{message}\n")
shift = int(input("Type the shift number:\n"))

test = []
for letter in message:
    if letter in alphabet:
        index = alphabet.index(letter)
        test.append(alphabet[index+shift])
print(f"\n{message}\n")
print(f"\n{test}\n")


# for a in range(len(message)):
#     if message[a] in alphabet:
#         print(a)
# print(f"\n{message}\n")

#TODO-1: 
    #Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.


#TODO-2: 
    #Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 