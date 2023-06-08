x = float(input("Please enter the first number: "))

oper = input("Please choose the operation: \n[ + ] Plus\n[ - ] Minus\n[ * ] Multiply\n[ / ] Divide \n[ ^ ] Square \n: ")

y = float(input("Please enter the second number: "))

opers_list = ["+", "-", "*", "/", "^"]

# logic here
# catch error by using ==> try except - method


result = 0
try:
    x/y
except ZeroDivisionError:
    print("ZeroDivisionError")
except:
    print("There is something wrong !!!")
else:
    if oper in opers_list:
        if oper == "+":
            result = x + y
        elif oper == "-":
            result = x - y
        elif oper == "*":
            result = x * y
        elif oper == "/":
            result = x / y
        elif oper == "^":
            result = x ** y
        else:
            print("There is something wrong !!!")

        # print result
        print(f"{x} {oper} {y} = {result}")
    else:
        print("Operator not found")
finally:
    print("Process end !")
