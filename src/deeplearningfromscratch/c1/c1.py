# numpy
import numpy as np

x = np.array([1,2,3,4])
y = np.array([1.,2.,3.,4.])

# element wise
print(x+y)
print(x-y)
print(x/y)
print(x*y)

# broadcast
print([1.0,2.0,3.0])
print(x / 2.0)

# 2d array
A = np.array([[1,2],[3,4]])
print(A)

print(A.shape)

print(A.dtype)

B = np.array([[1,2],[3,4]])
print(A+B)
print(A*B)
print(A-B)
print(A/B)

# broadcast
print(A*10)
print(A*np.array([10,20]))
print(A[0],A[0][0],A[0][1],A[1],A[1][0],A[1][1])

# flatten
A = np.array([[[1,2],[3,4]],[[1,2],[3,4]]])
Y = A.flatten()
print(Y)

# index array access
print(Y[np.array([0,2,4])])

# return bool array
print(type(A>2))
print(A > 2)

print(A[A>2])


# matplotlib

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,6,0.1)
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x,y1,label="sin")
plt.plot(x,y2,linestyle="--", label="cos")
plt.xlabel("x")
plt.ylabel('y')
plt.title("sin & cos")
plt.legend()
plt.show()


# image
from matplotlib.image import imread

img = imread('lena.jpeg')

plt.imshow(img)
plt.show()

