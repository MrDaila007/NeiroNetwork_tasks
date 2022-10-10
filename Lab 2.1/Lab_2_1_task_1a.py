a, b, c = int(input("Enter a ")), int(input("Enter b ")), int(input("Enter c "))
str = "Maximum number is"
if a > b:
    print(str,a) \
        if a > c \
        else print(str,c)
else:
    print(str,b) \
        if b > c \
        else print(str,c)