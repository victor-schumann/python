victory = '''
             V(-.o)V
       _      _                   
      (_)    | |                  
__   ___  ___| |_ ___  _ __ _   _ 
\ \ / / |/ __| __/ _ \| '__| | | |
 \ V /| | (__| || (_) | |  | |_| |
  \_/ |_|\___|\__\___/|_|   \__, |
                             __/ |
                            |___/ 
'''
draw = '''
     _                    
    | |                   
  __| |_ __ __ ___      __
 / _` | '__/ _` \ \ /\ / /
| (_| | | | (_| |\ V  V / 
 \__,_|_|  \__,_| \_/\_/  
'''
defeat = '''
     _       __           _   
    | |     / _|         | |  
  __| | ___| |_ ___  __ _| |_ 
 / _` |/ _ \  _/ _ \/ _` | __|
| (_| |  __/ ||  __/ (_| | |_ 
 \__,_|\___|_| \___|\__,_|\__|
 '''
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
hands=[rock, paper, scissors, rock]

print("Welcome to ROCK - PAPER - SCISSORS!!\nWhat do you choose?\n")
print("\t1 = rock\n\t2 = paper\n\t3 = scissors\n")
player = -1
player = int(input("choice: ")) -1

if player>3 or player<0:
    print("\nError! Obey the interval [1, 3]!")
    
else:
    computer = random.randint(0,2)
    print(f"\n\tyou play...{hands[player]}")
    print(f"\tcomputer plays...{hands[computer]}")

    if player == computer:
        print(f"\tthe result is...\n{draw}")
    
    elif hands[computer] == hands[player+1]:
        print(f"\tthe result is...\n{defeat}")
    
    else:
        print(f"\tthe result is...\n{victory}")