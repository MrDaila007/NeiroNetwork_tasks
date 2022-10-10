a = int(input("Enter a "))
b = int(input("Enter b "))
c = int(input("Enter c "))
str = "Number of coincidences"
if a == b == c:
    print(str, 3)
elif a == b or b == c or a == c:
    print(str, 2)
else:
    print(str, 0)