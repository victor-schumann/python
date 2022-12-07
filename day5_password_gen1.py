#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

#Input
#remember to pass this to a single input

print("Welcome to the PyPassword Generator!")

#passwd_def = input("How many LETTERS, SYMBOLS, and NUMBERS would you like in your password? (L S N)\n")

nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

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

#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
#print(f"{}")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P