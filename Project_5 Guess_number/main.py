# guess number - game

import random

comp_number = random.randint(1, 100)

## just to test game
print(comp_number)

# welcome
print("Welcome to Guess number game !!!")
print("If you want to exit program please enter >> x/q/exit <<")

steps = 0  # create global variable
while True:
    user_prompt = input("Please enter the whole number between 1-100\n: ")

    if user_prompt == "x" or user_prompt == "q" or user_prompt == "exit":
        print("Game end !")
        break
    else:
        user_prompt = int(user_prompt)  # change prompt type to integer

    steps += 1
    step_format = "Steps" if steps > 1 else "Step"  # detect plural or singular form

    if user_prompt == comp_number:
        print("You win !!!")
        print(f"{steps} - {step_format} for winning !")
        break
    elif user_prompt < comp_number:
        print("Your number is too low")
        print(f"Try: {steps} !")
    else:
        print("Your number is too higher")
        print(f"Try {steps} !")

    
