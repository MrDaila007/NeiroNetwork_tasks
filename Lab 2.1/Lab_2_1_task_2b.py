x = int(input("Number of km on first day: "))
y = int(input("Number of km for finish: "))
i = 1
while x < y:
    x *= 1.1
    i += 1
print("It will take:",i, "days")