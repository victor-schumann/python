# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
lowered_names=name1.lower()+name2.lower()

digit_one=lowered_names.count("t")+lowered_names.count("r")+lowered_names.count("u")+lowered_names.count("e")

digit_two=lowered_names.count("l")+lowered_names.count("o")+lowered_names.count("v")+lowered_names.count("e")

str_full_digit=str(digit_one)+str(digit_two)
full_digit=int(str_full_digit)

if full_digit>=40 and full_digit<=50:
    print(f"Your score is {full_digit}, you are alright together.")

elif full_digit<10 or full_digit>90:
    print(f"Your score is {full_digit}, you go together like coke and mentos.")

else:
    print(f"Your score is {full_digit}.")

