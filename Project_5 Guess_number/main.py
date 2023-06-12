# guess number - game

import random

comp_number = random.randint(1, 100)

# print(comp_number)

game_on = True
steps = 0
while game_on:
    user_prompt = int(input("Please enter the whole number between 1-100\n: "))
    steps += 1

    if user_prompt == comp_number:
        print("You win !!!")
        print(f"{steps}")
    elif user_prompt < comp_number:
        print("Too height")
