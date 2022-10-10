x = int(input("Enter fow much money you bring to bank"))
p = int(input("Percent of bank"))
y = int(input("Sum that you need"))
i = 0
while x < y:
    x *= 1 + p / 100
    x = int(100 * x) / 100
    i += 1
print("It will take", i, "years")