# create function which calculate factorial of numbers

def fact(n):
    if n == 1:
        return 1

    # call inner function
    return fact(n - 1) * n

print(fact(5))

# test function
test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result_list = [1, 2, 6, 24, 120, 720, 5040, 40320, 362880]

new_list = []
for i in test_list:
    x = fact(i)
    print(f"{i} - {x}")
    new_list.append(x)

print("\n")

# check matching
for i in range(len(new_list)):
    if new_list[i] == result_list[i]:
        print("GOOD")
    else:
        print("\tBAD")
