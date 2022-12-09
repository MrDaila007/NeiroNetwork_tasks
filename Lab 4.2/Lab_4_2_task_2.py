import numpy as np
def nonlin(x, deriv=False):
    if (deriv == True):
        return (x * (1 - x))

    return 1 / (1 + np.exp(-x))

X=np.array([[0.645,33,4,0.34],
           [2.880,152,14,1.5],
           [1.110,88,5,0.475],
           [10.400,260,3, 6],
           [2.880,152 ,3 , 1.5],
           [9.895,122,30,6.2],
           [3.695,136,3,3],
           [2.170,116,5 ,0.6],
           [27.895,278,150,11]])


y = np.array([[0],
              [0.5],
              [0],
              [1],
              [1],
              [0.5],
              [1],
              [0],
              [0.5]])


np.random.seed(1)

# случайно инициализируем веса, в среднем - 0
syn0 = 2 * np.random.random((4, 9)) - 1
syn1 = 2 * np.random.random((9, 1)) - 1


def normirovka (x,m1,m2):
    return (x-m1)/(m2-m1)

minX=np.min(X)
maxX=np.max(X)

for j in range(60000):

    # проходим вперёд по слоям 0, 1 и 2
    l0 = normirovka (X,minX,maxX)
    l1 = nonlin(np.dot(l0, syn0))
    l2 = nonlin(np.dot(l1, syn1))

    # как сильно мы ошиблись относительно нужной величины?
    l2_error = y - l2

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


X1=np.array([[74, 1050,1,90], # Белаз 1
            [13.6 ,260,10,3], # БТР80  1
            [2.88,152,14,1.5], # Газель пасс  0.5
            [27.895, 278,150, 11], # Лиаз-6213  0.5
            [0.3,40,3,0.25], # Урал мото  0
            [18.4,245,168,12]]) # Трамвай 0.5

l0 = normirovka(X1,minX,maxX)
l1 = nonlin(np.dot(l0, syn0))
l22 = np.dot(l1, syn1)
l2 = nonlin(l22)
print(np.round(l2,2))

