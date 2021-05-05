import random

number =random.randint(1,10)
"""
guess = int(input("please guess the number: "))

while number != guess:
    guess = int(input("uffs !! try again : guess again "))
else:
    print("you got it right congratulation!!!!")
"""

while True:
    guess =int(input("please guess the number"))
    if guess == number:
        print("la badhai xa")
    else:
        print("try again")