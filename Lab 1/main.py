import math

def sigmoid(x):
  return 1 / (1 + math.exp(-x))

#I1 = input()
#I2 =input()
I1=1
I2=0
I3=1
I4=0
print("I1",I1)
print("I2",I2)
print("I3",I3)
print("I4",I4)
w1=0.45
w2=0.78
w3=-0.12
w4=0.13
w5=1.5
w6=-2.3
n = 1
#print(a, b, c)

H1input = I1 * w1 + I2 * w3
H1output = sigmoid(H1input)
print("H1output",round(H1output, 2))

H2input = I1*w2+I2*w4
H2output = sigmoid(H2input)
print("H2output",round(H2output, 2))

O1input = H1output*w5+H2output*w6
O1output = sigmoid(O1input)
print("O_OUPUT",round(O1output, 2))

O1ideal = I1 ^ I2

Error = ((O1ideal - O1output) ** 2) / 1
print("ERROR",round(Error, 2))
