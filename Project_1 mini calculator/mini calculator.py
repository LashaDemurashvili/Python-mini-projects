x = float(input("Please enter the first number: "))

oper = input("Please choose the operation: \n[ + ] Plus\n[ - ] Minus\n[ * ] Multiply\n[ / ] Divide \n[ ^ ] Square \n: ")

y = float(input("Please enter the second number: "))

opers_list = ["+", "-", "*", "/", "^"]

# logic here
# catch error by using ==> try except - method

try:
    if oper in opers_list:
        if oper == "+":
            print(x + y)
        elif oper == "-":
            print(x - y)
        elif oper == "*":
            print(x * y)
        elif oper == "/":
            print(x / y)
        elif oper == "^":
            print(x ** y)
        else:
            print("There is something wrong !!!")
    else:
        print("There is something wrong !!!")
except:
    print("There is something wrong !!!")
