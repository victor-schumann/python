#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

#Input
#remember to pass this to a single input

print("Welcome to the PyPassword Generator!")

passwd_def = input("How many LETTERS, SYMBOLS, and NUMBERS would you like in your password? (L S N)\n").split()

for n in range(0, len(passwd_def)):
  passwd_def[n] = int(passwd_def[n])


nr_letters = passwd_def[0]
nr_symbols = passwd_def[1]
nr_numbers = passwd_def[2]

#test for positive int before proceeding
if nr_letters<0 or nr_numbers<0 or nr_symbols<0:
    print("\nERROR: One of the numbers you provided is negative, therefore you can't proceed! Try again with positive numbers!\n")
    
else:
    passwd = []
    for n in range(nr_letters):
        rand = letters[random.randint(0,len(letters)-1)]
        passwd.append(rand)
    
    for n in range(nr_symbols):
        rand = symbols[random.randint(0,len(symbols)-1)]
        passwd.append(rand)
    
    for n in range(nr_numbers):
        rand = numbers[random.randint(0,len(numbers)-1)]
        passwd.append(rand)
    
    random.shuffle(passwd)
    new_passwd = ''.join(passwd)
    print(f"{new_passwd}")