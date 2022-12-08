import random
import support

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
hangmen = [support.hangman0, support.hangman1, support.hangman2, support.hangman3, support.hangman4, support.hangman5, support.hangman6, " "]

word_list = ["butterfly", "baboon", "rock"]
word = word_list[random.randint(0,2)]
sketch = []
for x in word:
    sketch.append(" __")

print("  --- WELCOME TO THE HANGMAN ---")

if word == word_list[0]:
    print("\t\t--- HARD LEVEL ---")
    print(hangmen[0])
    print(" __ __ __ __ __ __ __ __ __\n")
elif word == word_list[1]:
    print("\t\t--- MEDIUM LEVEL ---")
    print(hangmen[0])
    print(" __ __ __ __ __ __\n")
else:
    print("\t\t--- EASY LEVEL ---")
    print(hangmen[0])
    print(" __ __ __ __\n")

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = support.isLetter()

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
score = 0
errors = 0

while score<len(set(word)) and errors<6:
    minus = 0
    plus = 0

    for a in range(len(word)):
        if guess == word[a]:
            sketch[a] = f" {guess}"
            plus+=1
        else:
            minus+=1
        

    if minus>0 and plus == 0:
        errors+=1

    elif plus>0:
        score+=1
        
    sketch_string = ""
    for char in sketch:
        sketch_string += char

    if errors<6:     
        print(hangmen[errors])
        print(f"\n{sketch_string.upper()}")
        print(f"SCORE: {score}\nERRORS: -{errors}")
    
        if score<len(set(word)) and errors<6:
            guess = support.isLetter()
        elif score==len(set(word)) and errors<6:
            print(support.congratulations)
    elif errors==6:
        print(support.game_over)
        print(hangmen[6])
        errors= 7



