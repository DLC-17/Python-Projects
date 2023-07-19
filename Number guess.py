#Number guess
#the game will generate a number 1-10, that the user is then prompted to guess and will be told if their guess was too high or whether it was too low
import random
def number_guess():
    computer_guess=random.randint(1,10)
    Player_guess=int(input("Take a guess 1-10: "))
    if Player_guess>computer_guess:
        print("That guess to high!")
    elif Player_guess==computer_guess:
        print("You got it right")
    else:
        print("That guess to low!")
