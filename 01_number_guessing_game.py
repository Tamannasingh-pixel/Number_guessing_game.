# ------------------ NUMBER GUESSING GAME ------------------
import random
from number_guessing_ascii import logo
from number_guessing_ascii import win
from number_guessing_ascii import lose

random_number = random.randint(1, 100)

print(logo)
print('''Welcome to Number Guessing Game!
I have a number in mind between 1 and 100.''')

level = input("There are two levels 'easy' and 'hard', make your choice:  ").lower()

if level == "easy":
    print("You have 10 chances to guess the number.")
    level = 10
    chances = 10
elif level == "hard":
    print("You have 5 chances to guess the number.")
    level = 5
    chances = 5
else:
    print("Invalid Input!")

def number_guessing():
    global chances
    global level
    chances -= 1
    attempts = (f"You have {chances} chances left.")
    guess = int(input("make a guess: "))

    if chances == 0:
        print(f"You have run out of guesses., the correct answer was {random_number}")
        print(lose)
    elif chances <= level:
        if guess <= 100:
            if guess == random_number:
                print("YAY!, you got the right answer, YOU WIN.")
                print(win)
            elif guess > random_number:
                print("too high!, guess again")
                print(attempts)
                number_guessing()
            elif guess < random_number:
                print("too low!, guess again")
                print(attempts)
                number_guessing()
    else:
        print("Invalid Input!")
number_guessing()
