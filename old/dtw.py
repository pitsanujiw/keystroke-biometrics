import numpy as np
from scipy.spatial.distance import euclidean
from fastdtw import fastdtw

x = np.array([[1,1], [2,2], [3,3], [4,4], [5,5]])
y = np.array([[2,2], [3,3], [4,4]])

a = (1, 2, 3, 5)
b = (4, 5, 6)

distance, path = fastdtw(a, b, dist=euclidean)
print(distance)
print(path)