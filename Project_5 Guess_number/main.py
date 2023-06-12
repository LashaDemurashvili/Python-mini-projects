# guess number - game

import random

comp_number = random.randint(1, 100)

## just to test game
# print(comp_number)

# welcome
print("Welcome to Guess number game !!!")
print("If you want to exit program please enter >> x/q/exit <<")

steps = 0  # create global variable
while True:
    user_prompt = input("Please enter the whole number between 1-100\n: ")

    if user_prompt == "x" or "q" or "exit":
        print("Game end !")
        break
    elif not user_prompt.isdigit():
        print("Please enter numbers !!!")
        continue  # continue - so start flow from beginning
    else:
        user_prompt = int(user_prompt)  # change prompt type to integer

    steps += 1  # iterate every step
    step_format = "Steps" if steps > 1 else "Step"  # detect plural or singular form

    if user_prompt == comp_number:
        print("You win !!!")
        print(f"{steps} - {step_format} for winning !")
        print("AWESOME" if steps <= 3 else "Not bad :)")
        break
    elif user_prompt < comp_number:
        print("Your number is too low")
    else:
        print("Your number is too higher")



