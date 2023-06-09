# Multiplication table using for loop

print(" Multiplication table ".center(40, "*"))
for i in range(1, 11):
    for j in range(1, 11):
        print(i * j, end="\t")
    print("\n")
    # print()  #we can use only print also
