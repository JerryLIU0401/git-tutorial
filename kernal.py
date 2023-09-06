import numpy
import numpy as np
import cv2

img = np.array([[1, 2, 3, 4, 5, 6],
       [2, 4, 6, 8, 10, 12],
       [3, 6, 9, 12, 15, 18],
       [4, 8, 12, 16, 20, 24],
       [5, 10, 15, 20, 25, 30],
       [6, 12, 18, 24, 30, 36]], dtype=np.uint8)

kernel = np.array(
          [[0, 0, 0],
          [1, 1, 1],
          [0, 0, 0]], dtype=np.uint8)
# Function
answer = cv2.filter2D(img, ddepth=-1, kernel=kernel) # ddepth 期望深度
print(answer[1:5, 1:5])
print(kernel.shape)
#

# For loop
l = img.shape[0] - kernel.shape[0] + 1 # y
l2 = img.shape[1] - kernel.shape[1] + 1 # x
result = np.zeros((l2, l))
for i in range (0, l):
    for j in range(0, l2):
        mat = img[i:i+l2-1,j:j+l-1]
        result[i][j] = numpy.multiply(mat, kernel).sum()

print(result.astype(int))
#