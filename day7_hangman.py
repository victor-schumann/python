import random
import support

#1 - Randomly choose a word from the word_list.
hangmen = [support.hangman0, support.hangman1, support.hangman2, support.hangman3, support.hangman4, support.hangman5, support.hangman6, " "]

word_list = ["rock", "baboon", "butterfly"]
r_index = random.randint(0,2)
word = word_list[r_index]
sketch = []

for x in word:
    sketch.append(" __")

#2 - Print the menu dinamically, according the chosen word.
print("  --- WELCOME TO THE HANGMAN ---")
lvl = ["\t\t--- EASY LEVEL ---", "\t\t--- MEDIUM LEVEL ---", "\t\t--- HARD LEVEL ---"]

print(lvl[r_index])
print(hangmen[0])
print(" __"*len(word))

#T3 - Ask the user to guess a letter.
guess = support.isLetter()

#4 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
score = 0
errors = 0

while score<len(word) and errors<6:
    if guess not in word:
        errors+=1
    
    for a in range(len(word)):
        if guess == word[a]:
            sketch[a] = f" {guess}"
            score+=1
        
    sketch_string = ""
    for char in sketch:
        sketch_string += char

#5 - Print the words according to the error and score counters
    if errors<6:     
        print(hangmen[errors])
        print(f"\n{sketch_string.upper()}")
        print(f"\nSCORE: \t\t{score}\nERRORS: \t{errors}")
    
        if score<len(word) and errors<6:
            guess = support.isLetter()
        elif score==len(word) and errors<6:
            print(support.congratulations)
            
    elif errors==6:
        print(support.game_over)
        print(hangmen[6])
        errors= 7