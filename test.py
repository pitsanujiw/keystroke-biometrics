import numpy as np
from scipy.spatial import euclidean

from fastdtw import fastdtw

x = np.array([[1,1], [2,2], [3,3], [4,4], [5,5]])
y = np.array([[2,2], [3,3], [4,4]])
distance.euclidean, path = fastdtw(x, y, dist=euclidean)

print(distance)