def hello():
    print('Hello, Python!')


def fibon(n):
    a = b = 1
    for i in range(n - 2):
        a, b = b, a + b
    print(b)


def discr(a, b, c):
    D = sqrt(b**2 - 4*a*c)
    x1 = (-b + D) / 2 * a
    x2 = (-b - D) / 2 * a
    print(f'x1 = {x1}', f'x2 = {x2}', sep='\n')


def sqrt(x):
    last_guess= x/2.0
    while True:
        guess= (last_guess + x/last_guess)/2
        if abs(guess - last_guess) < .000001: # example threshold
            return guess
        last_guess = guess
    #print(last_guess)