import numpy as np

def nonlin(x, deriv=False):
    if (deriv == True):
        return (x * (1 - x))

    return 1 / (1 + np.exp(-x))


X = np.array([[1111110, 1000000, 1000000, 1111100, 1000000, 1000000, 1000000, 1111110],#Е
              [11000, 100100, 100100, 100100, 100100, 100100, 1111110, 1000010],#Д
              [1000010, 1000010, 1000110, 1001010, 1010010, 1100010, 1000010, 1000010]])#И
y = np.array([[1, 0, 0],
              [0, 1, 0],
              [0, 0, 1]])
X = X / 10000000
y = y

np.random.seed(1)

# случайно инициализируем веса, в среднем - 0
syn0 = 2 * np.random.random((8, 20)) - 1
syn1 = 2 * np.random.random((20, 40)) - 1
syn2 = 2 * np.random.random((40, 3)) - 1

# print(syn0)
# print(syn1)

for j in range(80000):

    # проходим вперёд по слоям 0, 1 и 2
    l0 = X
    l11 = np.dot(l0, syn0)
    l1 = nonlin(l11)
    l22 = np.dot(l1, syn1)
    l2 = nonlin(l22)
    l33 = np.dot(l2, syn2)
    l3 = nonlin(l33)

    # как сильно мы ошиблись относительно нужной величины?
    l3_error = y - l3

    if (j % 5000) == 0:
        print("Error:" + str(np.mean(np.abs(l3_error))))

    # в какую сторону нужно двигаться?
    # если мы были уверены в предсказании, то сильно менять его не надо
    l3_delta = (l3_error) * nonlin(l3, deriv=True)

    # как сильно значения l1 влияют на ошибки в l2?
    l2_error = np.dot(l3_delta, syn2.T)
    l2_delta = (l2_error) * nonlin(l2, deriv=True)

    # в каком направлении нужно двигаться, чтобы прийти к l1?
    # если мы были уверены в предсказании, то сильно менять его не надо

    l1_error = np.dot(l2_delta, syn1.T)
    l1_delta = l1_error * nonlin(l1, deriv=True)

    syn2 += l2.T.dot(l3_delta)
    syn1 += l1.T.dot(l2_delta)
    syn0 += l0.T.dot(l1_delta)

# прогноз

X = np.array([[11000, 100100, 100100, 100100, 100100, 100100, 1110110, 1000010], #Д2
              [1111110, 1000000, 1000000, 1101100, 1000000, 1000000, 1000000, 1111110], #E2
              [1111111, 1111111, 1111111, 1111111, 1111111, 1111111, 1111111, 1111111]])
y = np.array([[0, 0, 0]])

X = X / 10000000
y = y

l0 = X
l11 = np.dot(l0, syn0)
l1 = nonlin(l11)
l22 = np.dot(l1, syn1)
l2 = nonlin(l22)
l33 = np.dot(l2, syn2)
l3 = nonlin(l33)

# как сильно мы ошиблись относительно нужной величины?
 #l2_error = y - l2
 #print(l2)

print('Прогноз')
print(np.round(l3,3))