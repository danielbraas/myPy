# the code was taken from Python Data Science Handbook: https://jakevdp.github.io/PythonDataScienceHandbook/02.05-computation-on-arrays-broadcasting.html

import numpy as np

a = np.array([0, 1, 2])
b = np.array([5, 5, 5])
a + b

a + 6

M = np.ones((3, 3))
M

M + a

a = np.arange(3)
b = np.arange(3)[:, np.newaxis]
a
b
a * b

M = np.ones((2, 3))
M
a = np.arange(3)
a
X = np.random.random((10, 3))
Xmean = X.mean(0)
Xmean

X_centered = X - Xmean
X_centered, X
X_centered.mean(0)

x = np.linspace(0, 5, 50)
y = np.linspace(0, 5, 50)[:, np.newaxis]

z = np.sin(x) ** 10 + np.cos(10 + y * x) * np.cos(x)

%matplotlib inline
import matplotlib.pyplot as plt

plt.imshow(z, origin='lower', extent=[0, 5, 0, 5],
           cmap='rainbow')
plt.colorbar();
