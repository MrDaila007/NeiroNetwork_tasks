import numpy as np
import math

def nonlin(x, deriv=False):
    if (deriv == True):
        return (x * (1 - x))

    return 1 / (1 + np.exp(-x))

X = np.array([[2.0655, 2.0796, 2.0923, 2.0980],
              [2.0796, 2.0923, 2.0980, 2.0980],
              [2.0923, 2.0980, 2.0980, 2.0980],
              [2.0980, 2.0980, 2.0980, 2.1049],
              [2.0980, 2.0980, 2.1049, 2.1190],
              [2.0980, 2.1049, 2.1190, 2.1161],
              [2.1049, 2.1190, 2.1161, 2.1105],
              [2.1190, 2.1161, 2.1105, 2.1071],
              [2.1161, 2.1105, 2.1071, 2.1071],
              [2.1105, 2.1071, 2.1071, 2.1071],
              [2.1071, 2.1071, 2.1071, 2.0989],
              [2.1071, 2.1071, 2.0989, 2.0915],
              [2.1071, 2.0989, 2.0915, 2.0845]])
y = np.array(
    [[2.0980, 2.0980, 2.1049, 2.1190, 2.1161, 2.1105, 2.1071, 2.1071, 2.1071, 2.0989, 2.0915, 2.0845, 2.0749]]).T



np.random.seed(1)

# случайно инициализируем веса, в среднем - 0
syn0 = 2 * np.random.random((4, 100)) - 1
syn1 = 2 * np.random.random((100, 1)) - 1


def normirovka (x):
    return (x-np.min(x))/(np.max(x)-np.min(x))

yy = normirovka (y)

for j in range(60000):

    # проходим вперёд по слоям 0, 1 и 2
    l0 = normirovka (X)
    l1 = nonlin(np.dot(l0, syn0))
    l2 = nonlin(np.dot(l1, syn1))

    # как сильно мы ошиблись относительно нужной величины?
    l2_error = yy - l2

    if (j % 10000) == 0:
        print ("Error:" + str(np.mean(np.abs(l2_error))))

    # в какую сторону нужно двигаться?
    # если мы были уверены в предсказании, то сильно менять его не надо
    l2_delta = l2_error * nonlin(l2, deriv=True)

    # как сильно значения l1 влияют на ошибки в l2?
    l1_error = np.dot(l2_delta, syn1.T)

    # в каком направлении нужно двигаться, чтобы прийти к l1?
    # если мы были уверены в предсказании, то сильно менять его не надо
    l1_delta = l1_error * nonlin(l1 , deriv=True)

    syn1 += l1.T.dot(l2_delta)
    syn0 += l0.T.dot(l1_delta)

# прогноз

X1 = np.array([[2.5481, 2.5481, 2.5590, 2.5741],
              [2.5481, 2.5590, 2.5741, 2.5886]
              ])
y1 = np.array([[2.5886],
              [2.5886]])
# нормировка значений X1, Y1 для прогноза с теми же коэффициентами
X1 = (X1-np.min(X))/(np.max(X)-np.min(X))
y1 = (y1-np.min(y))/(np.max(y)-np.min(y))

l0 = X1
l1 = nonlin(np.dot(l0, syn0))
l2 = nonlin(np.dot(l1, syn1))

# как сильно мы ошиблись относительно нужной величины?
l2_error = y1 - l2

print('ошибка прогноза (до обратной нормировки) ', l2_error)

# обратная нормировка
y2 = l2 * (np.max(y) - np.min(y)) + np.min(y)

print('Прогноз:  ', y2)


