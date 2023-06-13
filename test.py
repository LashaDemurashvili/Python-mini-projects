a = "1234"
b = "345"
a = a.split()
b = b.split()
a = set(a)
b = set(b)


print(a | b)
