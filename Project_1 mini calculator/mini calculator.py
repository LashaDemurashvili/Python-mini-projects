x = input("Please enter the first number: ")

oper = input("Please choose the operation: \n[ + ] Plus\n[ - ] Minus\n[ * ] Multiply\n[ / ] Divide \n[ ^ ] Square \n: ")

y = input("Please enter the second number: ")

oper_list = ["+", "-", "*", "/", "^"]


# logic here
# catch error by using ==> try except - method
result = 0
try:
    # if i choose letter instead of number this handler catching this error
    x = float(x)
    y = float(y)

except:
    print("Please enter only numbers !!!")
else:
    # handle zero division
    try:
        x / y
    except ZeroDivisionError:
        print("ZeroDivisionError")
    else:
        if oper in oper_list:
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
            print("Wrong operation !!!")
finally:
    print("Process end !")
