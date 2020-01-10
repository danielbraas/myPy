# This is taken from the Python Data Science Handbook - Aggregation functions in numpy

import numpy as np

L = np.random.random(100)
print(L);sum(L)
L, sum(L)

np.sum(L)
big_array = np.random.rand(1000000)
%timeit sum(big_array)
%timeit np.sum(big_array)

min(big_array), max(big_array)

%timeit big_array.sum()
