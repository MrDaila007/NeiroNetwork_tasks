n = int(input("Number to found NOD "))
i = 2
while n % i != 0:
    i += 1
print("NOD for", n, "is", i)