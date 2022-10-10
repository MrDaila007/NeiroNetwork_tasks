import math

def sigmoid(x):
  return 1 / (1 + math.exp(-x))

#I1 = input()
#I2 =input()
I1=1
I2=0
I3=0
I4=1
I5=1
I6=1
I7=0
I8=0

print("I1",I1)
print("I2",I2)
print("I3",I3)
print("I4",I4)
print("I5",I5)
print("I6",I6)
print("I7",I7)
print("I8",I8)

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

O1ideal1 = I1 ^ I2

########################################################
H3input = I3 * w1 + I4 * w3
H3output = sigmoid(H3input)
print("H1output",round(H3output, 2))

H4input = I3*w2+I4*w4
H4output = sigmoid(H4input)
print("H2output",round(H4input, 2))

O2input = H3output*w5+H4output*w6
O2output = sigmoid(O2input)
print("O_OUPUT",round(O2output, 2))

O2ideal2 = I3 ^ I4




H5input = I5 * w1 + I6 * w3
H5output = sigmoid(H5input)
print("H5output",round(H5output, 2))

H6input = I5*w2+I6*w4
H6output = sigmoid(H6input)
print("H2output",round(H6output, 2))

O3input = H5output*w5+H6output*w6
O3output = sigmoid(O3input)
print("O_OUPUT",round(O3output, 2))

O3ideal3 = I5 ^ I6



H7input = I7 * w1 + I8 * w3
H7output = sigmoid(H7input)
print("H7output",round(H7output, 2))

H8input = I7*w2+I8*w4
H8output = sigmoid(H8input)
print("H8output",round(H8output, 2))

O4input = H7output*w5+H8output*w6
O4output = sigmoid(O4input)
print("O_OUPUT",round(O4output, 2))

O4ideal4 = I7 ^ I8





Error = (((O1ideal1 - O1output) ** 2) + ((O2ideal2 - O2output) ** 2) + ((O3ideal3 - O4output) ** 2) + ((O4ideal4 - O4output) ** 2)) / 4
print("ERROR",round(Error, 2))
